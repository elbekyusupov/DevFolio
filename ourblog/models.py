from django.db import models
from ckeditor.fields import RichTextField
from account.models import User



# Create your models here.
class Skill(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class Personal(models.Model):
    img = models.ImageField(upload_to='personal', null=True, blank=True)
    name = models.CharField(blank=True, null=True, max_length=50)
    profile = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(blank=True, null=True, max_length=200)
    phone = models.CharField(max_length=15)
    skills = models.ManyToManyField(Skill)
    desc = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name




class Service(models.Model):
    icon = models.CharField(blank=True, null=True, max_length=30)
    title = models.CharField(blank=True, null=True, max_length=30)
    desc = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    img = models.ImageField(upload_to='blog', null=True, blank=True)
    type = models.CharField(blank=True, null=True, max_length=20)
    title = models.CharField(blank=True, null=True, max_length=100)
    desc = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    personal = models.ForeignKey(User, related_name='comment', null=True, blank=True, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comment', null=True, blank=True, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.personal.first_name

class Reply(models.Model):
    personal = models.ForeignKey(User, related_name='reply', null=True, blank=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name='reply', null=True, blank=True, on_delete=models.CASCADE)
    response = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.personal.first_name

class Category(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    price = models.FloatField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    k_price = models.FloatField(blank=True, null=True)
    img = models.ImageField(upload_to='products', default='default__images/user.png', null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, related_name='category',)


    def __str__(self):
        return self.name
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate = models.DateField()
    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    def __str__(self):
        return self.name


class  Cat(models.Model):
    name = models.CharField(max_length=300)
    parent = models.ForeignKey('self', related_name='childs', null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField(null=True, blank=True)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name