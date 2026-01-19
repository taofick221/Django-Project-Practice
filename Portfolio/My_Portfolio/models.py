from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(unique=True)
    enrolment_date=models.DateField(auto_now_add=True,null=True,blank=True)

class Profile(models.Model):
    bio=models.TextField()
    location=models.CharField(max_length=200)
    birth_date=models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.location)
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    message=models.TextField()

    
