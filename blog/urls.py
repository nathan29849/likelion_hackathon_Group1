from django.contrib import admin
from django.urls import path
from . import views


app_name="blog"

urlpatterns = [
    path('<int:id>/', views.detail, name="detail"),
    path('newreply', views.newreply, name="newreply"),
    path('replydelete/<int:id>', views.replydelete, name="replydelete"),
    path('rate/<str:rate>', views.rate, name="rate"),
]