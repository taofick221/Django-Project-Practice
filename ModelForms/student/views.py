from django.shortcuts import render,redirect,get_object_or_404
from .models import Student,Profile
from .forms import StudentForms,RegistrationForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# upload profile picture---->
def upload_image(request):
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Image uploaded successfully")
            return redirect('view_image')
        else:
            messages.error(request,"image not submited,please try again")
    else:
        form=ProfileForm()
    return render(request,'accounts/upload_profile.html',{'form':form})

# view profile picture-------->
def view_image(request):
    profiles=Profile.objects.all()
    return render(request,'accounts/view_profile.html',{'profiles':profiles})


# image delete---->
def image_delete(request,pk):
    image=get_object_or_404(Profile,pk=pk)
    if request.method=='POST':
        image.delete()
        messages.success(request,"Image is deleted")
        return redirect('view_image')
    return render(request,'accounts/image_delete.html',{'image':image})
        






# Registration start---->
def view_registration(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Registration successfull and login")
            return redirect('dashboard')
        else:
            messages.error(request,"Enter valid information")
    else:
        form=RegistrationForm()
    return render(request,'accounts/registration.html',{'form':form})

# Login function---->

def view_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successfull")
            return redirect('dashboard')
        else:
            messages.error(request,"Login failed,use valid username and password")
    return render(request,'accounts/login.html')

# logout function---->

def view_logout(request):
    logout(request)
    messages.success(request,"Logout successfull")
    return redirect('login')

# dashboard function--->
@login_required
def view_dashboard(request):
    return render(request,'accounts/dashboard.html')


# student list start----->

def student_create(request):
    form=StudentForms()
    if request.method=='POST':
        form=StudentForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student_list')
    return render(request,'student_form.html',{'form':form})

def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def student_details(request,pk):
    student=get_object_or_404(Student,pk=pk)
    return render(request,'student_details.html',{'student':student})

def student_edit(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        form=StudentForms(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('student_list')
    else:
        form=StudentForms(instance=student)
    return render(request,'student_form.html',{'form':form})

def student_delete(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=='POST':
        student.delete()
        messages.success(request,'Student delete successfully')
        return redirect('student_list')
    return render(request,'student_confirm_delete.html',{'student':student})    