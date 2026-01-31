from django.shortcuts import render
from .models import YoutubeUser
from django.core.cache import cache


def user_list(request):
    users=cache.get('user_data')
    if users is None:
        print("Cache miss:Fetching data from database")
        users=YoutubeUser.objects.all()
        cache.set('user_data',users,timeout=60)
    else:
        print("Cache hit:Fetching data from cache")
    return render(request,'data_list.html',{'users':users})
        


