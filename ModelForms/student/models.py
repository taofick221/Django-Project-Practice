from django.db import models

class Student(models.Model):
    Name=models.CharField()
    Age=models.IntegerField()
    Email=models.EmailField(unique=True)

    def __str__(self):
        return self.Name
    
