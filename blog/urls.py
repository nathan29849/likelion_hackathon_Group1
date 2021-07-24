from django.contrib import admin
from django.urls import path
from . import views


app_name="blog"

urlpatterns = [
    path('db', views.init_db, name="db"),
]