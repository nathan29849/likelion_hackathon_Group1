from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User
def login(request):
    if request.method == "POST": 
        # return render(request,'login.html')
        form = AuthenticationForm(request=request,data=request.POST)
        print(form)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(
            request=request,
            username=username,
            password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
        return redirect('account:login')
    else:
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})

def signup(request):
    if request.method=="POST":
        new_user = User()
        new_user.username = request.POST['username']
        new_user.password = request.POST['password']
        new_user.save()
        return redirect('home')
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')