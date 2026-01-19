from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Students,Contact


# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    student=Students.objects.all()
    return render(request,'about.html',{'student':student})


def contactpage(request):
    return render(request,'contact.html')

def submitcontact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        if name and email and message:
            Contact.objects.create(name=name,email=email,message=message)
            return HttpResponse(f"Thank you,{name},for your message")
        else:
            return HttpResponse("Please fill all the box")
    return redirect('contactpage')