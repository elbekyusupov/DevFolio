from django.shortcuts import render, redirect
from django.views import View
from . import  models
from django.db.models import Q,F
from .forms import NameForm
from django.core.mail import send_mail

# Create your views here.
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            print(form, sender)

            # recipients = ['info@example.com']
            # if cc_myself:
            #     recipients.append(sender)
            #
            # send_mail(subject, message, sender, recipients)
            return redirect('name')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    return render(request, 'name.html', {'form': form})
class InfoPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'information.html')

    def post(self, request, *args, **kwargs):
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        position = request.POST['position']
        region = request.POST['region']
        img = request.FILES.get("img")
        gender = request.POST['gender']
        agree = request.POST['check']
        models.Person.objects.create(fname=fname, lname=lname, email=email, position=position, region=region, img=img, gender=gender, agree=agree)

        return redirect('/person')

class PersonPage(View):
    def get(self, request, *args, **kwargs):
        persons = models.Person.objects.filter(fname = F('lname') )
        print(persons)
            # Q(fname__startswith='Yusupov') | Q(lname__startswith='Elbek')
        context = {
            'persons':persons
        }

        return render(request, 'person.html', context)

class UpdatePerson(View):
    def get(self, request, id, *args, **kwargs):
        person = models.Person.objects.filter(id = id).first()
        context = {
            "person" : person
        }
        return render(request, 'information.html', context)

    def post(self, request, id, *args, **kwargs):

        person = models.Person.objects.filter(id = id).first()
        print(person)
        person.fname = request.POST['fname']
        person.lname = request.POST['lname']
        person.email = request.POST['email']
        person.position = request.POST['position']
        person.region = request.POST['region']
        person.img = request.FILES.get("img")
        person.gender = request.POST['gender']
        person.agree = request.POST['check']
        person.save()

        return redirect('/person')

class DeletePerson(View):
    def get(self, request, id, *args, **kwargs):
        models.Person.objects.filter(id=id).first().delete()


        return redirect('/person')

    # def delete(self, request, id, *args, **kwargs):
    #     person = models.Person.objects.filter(id=id).first().delete()
    #     print('------',person)
    #     return redirect('/person')



