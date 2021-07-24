from django.shortcuts import render
import requests
from .models import Movie, Staff
# Create your views here.
def home(request):
    return render(request, 'home.html')

def index(request, ):
    return render(request, 'index.html')


def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    fields = ['title_kor', 'title_eng', 'poster_url', 'rating_aud', 'rating_cri', 'rating_net', 'genre', 'showtimes', 'release_date', 'rate', 'summary']
    
    staff_fields = ['name', 'role', 'image_url']
    for movie in movies:
        new_movie = Movie()
        new_movie.title_kor = movie["title_kor"]
        new_movie.title_eng = movie['title_eng']
        new_movie.poster_url = movie['poster_url']
        new_movie.rating_aud = movie['rating_aud']
        new_movie.rating_cri = movie['rating_cri']
        new_movie.rating_net = movie['rating_net']
        new_movie.genre = movie['genre']
        new_movie.showtimes = movie['showtimes']
        new_movie.release_date = movie['release_date']
        new_movie.rate = movie['rate']
        new_movie.summary = movie['summary']
        new_movie.save()

        staff_arr = movie["staff"]
    
        for staff in staff_arr:
            new_staff = Staff()
            new_staff.movie = new_movie
            new_staff.name = staff["name"]
            new_staff.role = staff["role"]
            new_staff.image_url = staff["image_url"]
            new_staff.save()

    return redirect('index')