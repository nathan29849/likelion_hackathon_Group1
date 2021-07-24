from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=100, null=True)
    poster_url = models.CharField(max_length=255, null=True)
    rating_aud = models.CharField(max_length=10)
    rating_cri = models.CharField(max_length=10)
    rating_net = models.CharField(max_length=10)
    genre = models.CharField(max_length=50)
    showtime = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    rate = models.CharField(max_length=50)
    summary = models.TextField()

class Staff(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="staffs")
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    image_url = models.CharField(max_length=255, null=True)

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment_date = models.DateTimeField(auto_now_add=True)  # 자동으로 데이터 생성 시간이 저장
    comment_body = models.TextField()

    class Meta:
        ordering = ['comment_date']     # 이렇게 하면 시간 순으로 정렬됨