from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LogoutView
from django.views import View
from django.views.generic import TemplateView,CreateView

# Create your views here.
class AbautMeV(TemplateView):
    template_name = "myauth/abaut-me.html"


class RegUser(CreateView):
    model = User
    form_class=UserCreationForm
    template_name = "myauth/RegUser.html"
    success_url = reverse_lazy("myauth:abaut_me")

    def form_valid(self, form):
        response=super().form_valid(form)
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return response

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
    return HttpResponse(f"Cookie value: {value!r}")

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


class FromTest(View):
    def get(self, request)->JsonResponse:
        return JsonResponse({"foo":"bar","spam":"eggs"})
