from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.view_registration, name='registration'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout'),
    path('dashboard', views.view_dashboard, name='dashboard'),

    path('upload/', views.upload_image, name='upload_image'),
    path('profile/', views.view_image, name='view_image'),
    path('delete/<int:pk>/', views.image_delete, name='image_delete'),
    
    path('', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('detail/<int:pk>/', views.student_details, name='student_details'),
    path('edit/<int:pk>/', views.student_edit, name='student_edit'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
]
