from . import views
from django.urls import path,re_path

urlpatterns = [
    path('post/<int:post_id>/',views.post_details,name='post_details'),
    path('user/<str:username>/',views.user_profile,name='user_profile'),
    re_path(r'^airticle/(?P<year>[0-9]{4})/$',views.airticle_year,name='airticle_year'),


]

