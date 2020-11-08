from django.contrib import admin
from django.urls import path
from .views import PageView

urlpatterns = [
    path('pageinfo',PageView, name="PView"),
]