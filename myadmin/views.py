from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.models import Account
from student.models import StudentProfile
from .models import StudentMark

def adminLogin(request):
    if request.user.is_authenticated and request.user.is_admin:
        return redirect('adminhome')
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_admin:
            login(request,user)
            return redirect('adminhome')
        else:
            return redirect('adminlogin')
    return render(request, 'adminlogin.html')


def adminHome(request):
    student=Account.objects.all()
    prof = StudentProfile.objects.filter(student=request.user)
    context={
        'students':student,
        'prof':prof
    }
    return render(request,'adminHome.html', context)
    


def adminLogout(request):
    logout(request)
    return redirect('adminlogin')




def MarksAdd(request):
    if request.method=="POST":
        marks=request.POST.get('marks')
        user=request.user
        stud=StudentMark.objects.create(student=user, marks=marks)
        stud.save()
        return redirect('adminhome')
    return render(request, 'addMarks.html')



def MarksEdit(request,id):
    mark= StudentMark.objects.get(id=id)
    if request.method=="POST":
        mark.marks=request.POST.get('marks')
        mark.save()
        return redirect('adminhome')

    return redirect(request,'editmarks.html')

    