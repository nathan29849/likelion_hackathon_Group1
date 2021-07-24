from django.contrib import admin
from .models import Movie, Staff, Comment
# Register your models here.
admin.site.register(Movie)
admin.site.register(Staff)
admin.site.register(Comment)