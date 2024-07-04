from django.urls import path
from django.contrib.auth.views import LoginView

from myauth.views import user_login_v1,set_cookie_view,get_cookie_view,set_session_v,get_session_v,logout_user,MyLogout


app_name="myauth"

urlpatterns = [
path('login_v1/',user_login_v1,name='login_v1'),
path('login_v2/',
     LoginView.as_view(
         template_name="myauth/loginF2.html",
         redirect_authenticated_user=True,
     ),
     name='login_v2'),
path('set_c/',set_cookie_view,name='set_c'),
path('get_c/',get_cookie_view,name='get_c'),

path('set_s/',set_session_v,name='set_s'),
path('get_s/',get_session_v,name='get_s'),

# path('log_out/',logout_user,name='log_out_usr'),
path('log_out_v2/',MyLogout.as_view(),name='log_out_usr_v2'),
    ]
