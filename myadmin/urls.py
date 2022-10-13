from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminLogin, name="adminlogin"),
    path("adminhome", views.adminHome, name="adminhome"),
    path("adminout", views.adminLogout, name="adminout"),
    path("addmarks", views.MarksAdd, name="addmarks"),
    path("editmarks/<int:id>", views.MarksEdit, name="editmarks"),
]
