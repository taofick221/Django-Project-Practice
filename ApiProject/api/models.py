from django.db import models

# class Student(models.Model):
#     name=models.CharField(max_length=100)
#     age=models.IntegerField()
#     email=models.EmailField(unique=True)

#     def __str__(self):
#         return self.name



# For class based view api--->

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    city=models.CharField(max_length=50,default="Unknown")

    def __str__(self):
        return self.name
    
    
