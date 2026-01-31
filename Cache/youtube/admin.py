from django.contrib import admin
from .models import YoutubeUser
from django.core.cache import cache
from django.contrib import messages

@admin.action(description='clear users cache')
def case_clear(modeladmin,request,queryset):
    cache.delete('user_data')
    messages.success(request,"Users data clear successfully")


@admin.register(YoutubeUser)
class YoutubeUserAdmin(admin.ModelAdmin):
    list_display=('name','email','subscribe')
    actions=[case_clear]