# from django.urls import path
# from . import views

# urlpatterns = [
#     path('students/',views.get_students,name='get_students'),
#     path('students/add/',views.add_students,name='add_students'),
#     path('students/update/<int:pk>/',views.update_students,name='update_students'),
#     path('students/delete/<int:pk>/',views.delete_students,name='delete_students'),
    
# ]


# # For class based view api--->

# from django.urls import path
# from .views import StudentAPI

# urlpatterns = [
#     path('student/',StudentAPI.as_view()),
#     path('student/<int:pk>/',StudentAPI.as_view()),
# ]



# Generic API view and mixin urls path---------------->
from django.urls import path
from .views import StudentListCreateAPI,StudentRetriveUpdateDelete

urlpatterns = [
    path('student/',StudentListCreateAPI.as_view()),
    path('student/<int:pk>/',StudentRetriveUpdateDelete.as_view()),
]
