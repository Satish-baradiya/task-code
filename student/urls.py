from os import name
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("students/<int:pk>",views.student,name="student"),
    path("getpdf",views.getpdf,name="getpdf")
]