from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contactpage,name='contactpage'),
    path('submitcontact/',views.submitcontact,name='submitcontact'),
    
]
