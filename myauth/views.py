from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LogoutView

# Create your views here.
def user_login_v1(request:HttpRequest)->HttpResponse:
    if request.method=="GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request,'myauth/loginF1.html')
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect("/admin/")

    return render(request,"myauth/loginF1.html",{"error":"Ошибка"})

def set_cookie_view(request:HttpRequest)->HttpResponse:
    response=HttpResponse("Cookie set")
    response.set_cookie("fizz","buzz",max_age=3600)
    return response


def get_cookie_view(request:HttpRequest)->HttpResponse:
    value=request.COOKIES.get("fizz","default value")
    return HttpResponse(f"Куки: {value!r}")

def set_session_v(request:HttpRequest)->HttpResponse:
    request.session["foobar"]="spamaggs"
    return HttpResponse("Session set!")


def get_session_v(request:HttpRequest)->HttpResponse:
    data=request.session.get("foobar","default data")
    return HttpResponse(f"Session data: {data!r}")

def logout_user(request:HttpRequest)->HttpResponse:
    logout(request)
    return redirect(reverse("myauth:login_v2"))

class MyLogout(LogoutView):
    next_page = reverse_lazy("myauth:login_v2")
