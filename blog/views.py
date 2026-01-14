from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
def home(request):
    context={
        "name":"Md taofick",
        "age":23,
        "skill":["python","java","database"],
        "user":User("taofick",23),
        "blog":{
            "title":"shop",
            "description":"<b>Welcome to our shop</b>",
            "created_at": datetime(2025,11,12,10,12)
        },
        "empty_value":None,
    }
    return render(request,'blog/blog_list.html',context)
