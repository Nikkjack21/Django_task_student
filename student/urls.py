from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginStudent, name="login"),
    path("register", views.RegisterStudent, name="register"),
    path("home", views.StudentHome, name="home"),
    path("logout", views.StudentLogout, name="logout"),
    path("profile", views.showProfile, name="profile"),
    path("add-profile", views.AddProfileInfo, name="add"),
]
