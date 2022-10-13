from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from student.models import StudentProfile

# Create your views here.


def RegisterStudent(request):

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = Account.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
        user.save()
        return redirect("login")

    return render(request, "register.html")


def LoginStudent(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return redirect("login")

    return render(request, "login.html")


@login_required(login_url="login")
def StudentHome(request):

    return render(request, "index.html")


def StudentLogout(request):
    logout(request)
    return redirect("login")


def showProfile(request):
    profile = StudentProfile.objects.filter(student=request.user)
    if not profile:
        return redirect("add")
    context = {"profile": profile}
    return render(request, "profile.html", context)


def AddProfileInfo(request):
    profile = StudentProfile.objects.filter(student=request.user)

    if request.method == "POST":
        student = request.user
        address = request.POST.get("address")
        dob = request.POST.get("dob")
        image = request.FILES.get("image")
        phone = request.POST.get("phone")
        profile = StudentProfile.objects.create(
            student=student, address=address, dob=dob, image=image, phone=phone
        )
        profile.save()
        return redirect("home")

    return render(request, "addProfile.html")
