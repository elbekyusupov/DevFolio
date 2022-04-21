from django.shortcuts import render, redirect
from django.views import View
from . import  models
from django.db.models import Q,F, Avg, Max, FloatField, Count, Min, Sum
from django.contrib.auth import authenticate, logout, login
from account.models import User
# from django.http import HttpResponseRedirect

# Create your views here.
class RegisterPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        phone = request.POST['phone']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if len(phone) >= 9 and password == password2 :
            user = User.objects.create_user(phone=phone, password=password, first_name=first_name, last_name=last_name, email = email)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')

class LoginPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')
    
    def post(self, request, *args, **kwargs):
        phone = request.POST['phone']
        user = User.objects.filter(phone = phone,).first()
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('register')

class LogoutPage(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')

class ProfilePage(View):
    def get(self, request, *args, **kwargs):

        user = request.user
        if user.is_authenticated:
            context = {
                'us' : user
            }
            return render(request, 'profile.html', context)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user = User.objects.filter(phone=request.user.phone).first()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.birthday = request.POST['birthday']
            user.email = request.POST['email']
            user.address = request.POST['address']
            user.avatar = request.FILES['avatar']
            user.gender = request.POST['gender']
            user.save()

            return redirect('home')
        else:
            return redirect('login')
        


class HomePage(View):
    def get(self, request, *args, **kwargs):
        personal = models.Personal.objects.first()
        services = models.Service.objects.all()
        blogs = models.Blog.objects.all()

        context = {
            'personal': personal,
            'services': services,
            'blogs': blogs,

        }
        return render(request, 'home.html', context)

class BlogPage(View):

    def get(self, request, id,  *args, **kwargs):
            personal = None
            blog = models.Blog.objects.filter(id = id).first()
            if request.user.is_authenticated:
                personal = request.user

            context = {
                'blog': blog,
                'personal': personal,
            }
            return render(request, 'blog-single.html', context)

    def post(self, request, id,  *args, **kwargs):
        user = request.user

        if request.user.is_authenticated:
            blog = models.Blog.objects.filter(id = id).first()
            text = request.POST['text']

            models.Comment.objects.create(text=text, personal=user, blog=blog)

            return redirect('blog', blog.id)
        else:
            return redirect('login')

class ReplyPage(View):
    def get(self, request, id,  *args, **kwargs):
        comment = models.Comment.objects.filter(id = id).first()
        context = {
            'comment':comment,
        }
        return render(request, 'reply.html', context)

    def post(self, request, id,  *args, **kwargs):
        comment = models.Comment.objects.filter(id = id).first()
        res = request.POST['text']
        models.Reply.objects.create(response=res, personal=request.user, comment=comment)

        return redirect('blog', comment.blog.id)

class CommentPage(View):
    def get(self, request, id,  *args, **kwargs):
        comment = models.Comment.objects.filter(id = id).first()
        context = {

            'comment':comment,
        }
        return render(request, 'comment.html', context)

    def post(self, request, id,  *args, **kwargs):
        comment = models.Comment.objects.filter(id = id).first()
        comment.text = request.POST['text']
        comment.save()
        return redirect('blog', comment.blog.id)

class DeleteCommentPage(View):
    def get(self, request, id,  *args, **kwargs):
        comment = models.Comment.objects.filter(id = id).first()
        comment.delete()

        return redirect('blog', comment.blog.id)

class ProductPage(View):
    def get(self, request, *args, **kwargs):
        products = models.Product.objects.all()
        product1 = models.Category.objects.annotate(total_sum=Sum(F('category__price') * F('category__count')))

        context = {
            'products':products,
            'product1':product1[0].total_sum,
            # 'product2':product2,
            # 'product3':product3,
            # 'product4':product4,
            # 'product5':product5,
            # 'product6':product6,
            # 'product7':product7,
            # 'product8':product8,
            # 'product9':product9,
            # 'product10':product10,

        }
        return render(request, 'product.html', context)

    # Category.objects.aggregate(total_count=Sum('category__count'))
    # total_count : 1218

    # Author.objects.annotate(total_pages=Sum('book__pages'))
    # product1[1].total_pages -- > 1177
    #

    # Store.objects.aggregate(young_age=Min('books__authors__age'))
    # {'young_age': 50}

    # Store.objects.aggregate(min_price=Min('books__price'), max_price=Max('books__price'))
    # {'min_price': Decimal('26000'), 'max_price': Decimal('50000')}

    # Book.objects.all().aggregate(Avg('pages'), Max('pages'), Min('pages'))
    # {'pages__avg': 335.4, 'pages__max': 544, 'pages__min': 200}

    # Book.objects.all().aggregate(Avg('pages'))
    # {'pages__avg': 335.4}

    # Publisher.objects.annotate(num_books=Count('book'))
    # print (product1[0].num_books)
    # 3

    #
    # product1 = models.Book.objects.all().aggregate(max_price=Max('price'))
    # {'max_price': Decimal('56000')}

    # Book.objects.all().aggregate(Avg('price'))
    # {'price__avg': Decimal('40000')}

    # product1 = models.Book.objects.filter(publisher__name = 'Hilol nashr').count()
    # 3

    # Category.objects.annotate(num_phones = Count('category')).order_by('-num_phones')[:5]
    # print (product1[0].name , "  ", product1[0].num_phones)
    # Redmi    4

    # models.Category.objects.annotate(num_phones = Count('category')) <Category: Samsung>, <Category: Iphone>,..
    # print (product1[0].num_phones)

    # aggregate(quantity = Avg('count')) {'quantity': 135.33333333333334}
    # aggregate(Avg('count')) {'count__avg': 135.33333333333334}
    # filter(category__name = 'Redmi').count() res -> 4
    # product2 = models.Product.objects.filter(price__gte = F('k_price')*2)
    # product3 = models.Product.objects.filter(count__gte = 10, discount__lt = 5, discount__gt = 10)
    # product4 = models.Product.objects.filter(Q(k_price = F('price')) | Q(discount__gt = 10))
    # product5 = models.Product.objects.filter(Q(k_price = F('price')) , Q(discount__gt = 0))
    # product6 = models.Product.objects.filter( Q(count = 0), (Q(k_price__gt = 2000000) | Q(price__gt = 2500000)))
    # product7 = models.Product.objects.filter( Q(discount__gt = 10), Q(count__gte = 100) | Q(price__gte = 50000) | Q(k_price__gt = 100000))
    # product8 = models.Product.objects.filter(k_price__lt = F('price')-500000 , discount__gt = 5, k_price__gte = 200000)
    # product9 = models.Product.objects.filter(k_price__lte = F('price')*(100-F('discount')))
    # product10 = models.Product.objects.filter(k_price__lte = F('price')*(100-F('discount')*2))
