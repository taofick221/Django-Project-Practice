from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def post_details(request,post_id):
    return HttpResponse(f"Blog number is:{post_id}")
def user_profile(request,username):
    return HttpResponse(f"User name is: {username}")
def airticle_year(request,year):
    return HttpResponse(f"Airticle published year is: {year}")
