from django.db import models

class Student(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Email=models.EmailField(unique=True)

    def __str__(self):
        return self.Name
    
class Profile(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name