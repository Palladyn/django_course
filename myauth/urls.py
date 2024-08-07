from django.urls import path
from django.contrib.auth.views import LoginView

from myauth.views import user_login_v1,set_cookie_view,get_cookie_view,set_session_v,get_session_v,logout_user,\
    MyLogout,AbautMeV,RegUser,FromTest,HelloView,HelloView1,HelloView2


app_name="myauth"

urlpatterns = [
path('login_v1/',user_login_v1,name='login_v1'),
path('login_v2/',
     LoginView.as_view(
         template_name="myauth/loginF2.html",
         redirect_authenticated_user=True,
     ),
     name='login_v2'),
# path('log_out/',logout_user,name='log_out_usr'),
path('log_out_v2/',MyLogout.as_view(),name='log_out_usr_v2'),

path('set_c/',set_cookie_view,name='set_c'),
path('get_c/',get_cookie_view,name='get_c'),

path('set_s/',set_session_v,name='set_s'),
path('get_s/',get_session_v,name='get_s'),

path('abaut_me/',AbautMeV.as_view(), name='abaut_me'),

path('reg_usr/',RegUser.as_view(), name='reg_usr'),

path('tst_json/',FromTest.as_view(), name='tst_json'),

path('hello_v/',HelloView.as_view(), name='hello_view'),
path('hello_v1/',HelloView1.as_view(), name='hello_view1'),
path('hello_v2/',HelloView2.as_view(), name='hello_view2'),




    ]
