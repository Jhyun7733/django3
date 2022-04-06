from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# 태그 /메시지 
def update(request):

    if request.method == "POST":
        u = request.user
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        if up:
            u.set_password(up)
        u.comment = uc
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        login(request, u)
        return redirect("acc:profile")

    return render(request, "acc/update.html")

# Create your views here
def delete(request):
    u = request.user
    ck = request.POST.get("pwck")
    if check_password(ck, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.info(request, "계정 정보가 맞지 않습니다.")
        return redirect("acc:profile")


def profile(request):
    return render(request, "acc/profile.html")

def signup(request):

    if request.method =="POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        pi = request.FILES.get("upic")
        print(un, up, uc, pi)
        User.objects.create_user(username=un, password=up, comment=uc, pic=pi)
        return redirect("acc:login")
    return render(request, "acc/signup.html")

def logout_user(request):
    logout(request)
    return redirect("acc:login")

def index(request):
    return render(request, "acc/index.html")

def login_user(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f"{u} 환영합니다.")
            return redirect("acc:index")
        else:
            messages.error(request, "계정 정보가 맞지 않습니다.")
    return render(request, "acc/login.html")