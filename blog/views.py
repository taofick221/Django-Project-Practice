from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
def home(request):
    blog=[
        {"title":"Django","featured":True,"author":"Taofick"},
        {"title":"python","featured":False,"author":"Taofick"},
        {"title":"fastapi","featured":False,"author":"Taofick"},
    ]
    context={
        "blog":blog,
        "name":"Md taofick",
        "age":23,
        "skill":["python","java","database"],
        "user":User("taofick",23),
        "empty_value":None,
    }
    return render(request,'blog/blog_list.html',context)
