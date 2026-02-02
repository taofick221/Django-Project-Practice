# from django.shortcuts import render
# from .models import Student
# from .serializers import StudentSerializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# @api_view(['GET'])
# def get_students(request):
#     students=Student.objects.all()
#     serializer= StudentSerializers(students,many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_students(request):
#     serializer=StudentSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT','PATCH'])
# def update_students(request,pk):
#     try:
#         students=Student.objects.get(id=pk)
#     except Student.DoesNotExist:
#         return Response({"error":"Student not found"},status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method=='PATCH':
#         serializer=StudentSerializers(students,data=request.data,partial=True)
#     else:
#         serializer=StudentSerializers(students,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_students(request,pk):
#     try:
#         students=Student.objects.get(id=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     students.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)








# # For class based view api--->

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import StudentSerializers
# from .models import Student


# class StudentAPI(APIView):
    
#     def get(self,request,pk=None):
#         if pk:
#             try:
#                 student=Student.objects.get(id=pk)
#                 serializer=StudentSerializers(student)
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             except Student.DoesNotExist:
#                 return Response({"error":"Student not found"},status=status.HTTP_400_BAD_REQUEST)
#         else:
#             # read all data
#             student=Student.objects.all()
#             serializer=StudentSerializers(student,many=True)
#             return Response(serializer.data,status=status.HTTP_200_OK)
    

#     # post request
#     def post(self,request):
#         serializer=StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

#     # put request
#     def put(self,request,pk):

#         try:
#             student=Student.objects.get(id=pk)
#             serializer=StudentSerializers(student,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
#         except Student.DoesNotExist:
#             return Response({"error":"Student not found"},status=status.HTTP_400_BAD_REQUEST)
    
#     # delete request
#     def delete(self,request,pk):
#         try:
#             student=Student.objects.get(id=pk)
#         except Student.DoesNotExist:
#             return Response({"error":"Student not found"},status=status.HTTP_400_BAD_REQUEST)

#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







# Generic API view and mixin---------------->

from rest_framework import generics,mixins
from .models import Student
from .serializers import StudentSerializers

class StudentListCreateAPI(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    # Get all data----->
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    # Create new data---->
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
    

class StudentRetriveUpdateDelete(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    
    # get single data----->
    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    # update old data---->
    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    # delete data----->
    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    
