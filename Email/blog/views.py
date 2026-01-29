from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

# def send_email(request):
#     subject="Welcome to my blog"
#     message="Thanks you for subscribing to  my blog"
#     from_email="mdtaofick45418@gmail.com"
#     recipient_list=["rahaman35-847@diu.edu.bd"]
#     send_mail(subject,message,from_email,recipient_list)
#     return HttpResponse("Your email is send successfully")

def send_email(request):
    subject="Welcome to my blog"
    message=render_to_string('email/welcome_email.html',{'username':'Taofick','blog':'My blog',})
    email=EmailMessage(subject,message,"mdtaofick45418@gmail.com",["rahaman35-847@diu.edu.bd"])
    email.content_subtype="html"
    email.send()
    return HttpResponse("Email sent")
