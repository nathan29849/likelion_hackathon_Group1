from django.shortcuts import render, get_object_or_404, redirect
import requests
from .models import Movie, Staff, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    movies = Movie.objects.order_by('-release_date')
    paginator = Paginator(movies, 8)
    page = request.GET.get('page')
    paginated_movies = paginator.get_page(page)
    for movie in paginated_movies:
        if movie.rating_aud != "준비중":
            movie.int_rating_aud = round(float(movie.rating_aud))
            print(movie.int_rating_aud)
    return render(request, 'home.html', {'movies': paginated_movies})

def rate(request, rate):
    movies = Movie.objects.filter(rate=rate)
    paginator = Paginator(movies, 8)
    page = request.GET.get('page')
    paginated_movies = paginator.get_page(page)
    for movie in paginated_movies:
        if movie.rating_aud != "준비중":
            movie.int_rating_aud = round(float(movie.rating_aud))
            print(movie.int_rating_aud)
    return render(request, 'home.html', {'movies': paginated_movies})

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
        print(len(movie['rating_cri']))
        if len(movie['rating_aud']) > 2:
            new_movie.rating_aud = movie['rating_aud']
        else:
            new_movie.rating_aud = "준비중"

        if len(movie['rating_cri']) > 2:
            new_movie.rating_cri = movie['rating_cri']
        else:
            new_movie.rating_cri = "준비중"
        
        if len(movie['rating_net']) > 2:
            new_movie.rating_net = movie['rating_net']
        else:
            new_movie.rating_net = "준비중"

        if len(movie['genre']) > 2:
            new_movie.genre = movie['genre']
        else:
            new_movie.genre = "준비중"            
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
        
    return redirect('home')

def detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    return render(request, 'detail_1.html', {"movie": movie})


def newreply(request):
    if request.method == "POST":
        comment = Comment()
        comment.comment_body = request.POST['comment_body']
        comment.movie = Movie.objects.get(pk = request.POST['movie'])
        user = request.POST['user']
        if user:
            comment.user = User.objects.get(username=user)
        else:
            return redirect('account:login')    # 로그인 창으로 이동
        comment.save()

        return redirect("blog:detail", comment.movie.id)
    else:
        return redirect('home')

def replydelete(request, id):       # comment.id 받아옴
    comment = get_object_or_404(Comment, pk=id)
    movie_id = comment.movie.id
    comment.delete()
    return redirect('blog:detail', movie_id)

def search(request):
    keyword = request.GET.get('keyword')
    movies = Movie.objects.filter(title_kor__contains=keyword)
    paginator = Paginator(movies, 8)
    page = request.GET.get('page')
    paginated_movies = paginator.get_page(page)
<<<<<<< HEAD
    return render(request, 'home.html', {'movies': paginated_movies, 'keyword': keyword})
=======
    for movie in paginated_movies:
        if movie.rating_aud != "준비중":
            movie.int_rating_aud = round(float(movie.rating_aud))
            print(movie.int_rating_aud)
    return render(request, 'home.html', {'movies': paginated_movies, 'keyword':keyword})
>>>>>>> 9ca5d614427c61f9e452714016d4c821eae05cb6


