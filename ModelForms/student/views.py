from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .forms import StudentForms
from django.contrib import messages

def student_create(request):
    form=StudentForms()
    if request.method=='POST':
        form=StudentForms(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'student_success.html')
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