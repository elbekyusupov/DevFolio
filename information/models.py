from django.db import models

# Create your models here.
class Person(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 200)
    position = models.CharField(max_length = 50)
    region = models.CharField(max_length = 50)
    img = models.ImageField(upload_to='person', null=True, blank=True)
    gender = models.CharField(max_length = 10)
    agree = models.IntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.fname + ' ' + self.lname




