from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# urlpatterns = [
#     path('public/',views.public_view,name='public_view'),
#     path('private/',views.private_view,name='private_view')
# ]


# for session authentication
# urlpatterns = [
#     path('blog/',views.blog_list,name='blog_list'),
# ]


# for auth token 
urlpatterns = [
    path('auth-token/',obtain_auth_token,name='api_token_auth'),
    path('profile/',views.profile,name='profile'),
    path('admin/',views.admin,name='admin'),
]
