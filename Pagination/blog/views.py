from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.http import HttpResponse

def post_list(request):
    post=Post.objects.all().order_by('id')
    paginator=Paginator(post,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'post_list.html',{'page_obj':page_obj})


# session set, get and delete------->
def set_session(request):
    request.session['username']='taofick'
    request.session['age']='23'
    return HttpResponse("Session data is set")
def get_session(request):
    username=request.session.get('username','guest')
    age=request.session.get('age','not define')
    return HttpResponse(f"Welcome {username} and your age is {age}")
def delete_session(request):
    request.session.flush()
    return HttpResponse("Session deleted")


# cookie set, get and delete------->
def set_cookie(request):
    response= HttpResponse("Cookie set successfully")
    response.set_cookie('username','Taofick',max_age=60)
    response.set_cookie('age','23',max_age=60)
    return response
def get_cookie(request):
    username=request.COOKIES.get('username','guest')
    age=request.COOKIES.get('age','Not define')
    return HttpResponse(f"Welcome {username} and your age is {age}")

def delete_cookie(request):
    response=HttpResponse("Cookie delete successfully")
    response.delete_cookie('username')
    response.delete_cookie('age')
    return response

