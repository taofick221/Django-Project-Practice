# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny,IsAuthenticated
# from api.models import Student
# from api.serializers import StudentSerializers

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def public_view(request):
#     return Response({"message":"This is public view"})


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def private_view(request):
#     return Response({"message":f"Hello {request.user.username}."})




# for session authentication and isauthenticatedoreadonly----->
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from api.models import Student
# from api.serializers import StudentSerializers

# @api_view(['GET','POST'])
# def blog_list(request):
#     if request.method=='GET':
#         blogs=Student.objects.all()
#         serializer=StudentSerializers(blogs,many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




# auth token
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authtoken.models import Token

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user=request.user
    return Response({
        "username":user.username,
        "email":user.email,
        "is_staff":user.is_staff,
    })

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin(request):
    return Response("Welcome to admin panel")