from . import views
from django.urls import path

urlpatterns = [
    path('',views.blog_list,name='blog_list'),
]
