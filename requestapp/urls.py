from django.urls import path

from requestapp.views import process_get_view,user_form_view,upload_file_view,new_user_form_view,new_upload_file_view

app_name="requestapp"

urlpatterns = [
path('get/',process_get_view,name='get_req'),
path('post/',user_form_view,name='post_req'),
path('upload_f/',upload_file_view,name='upload_f_req'),
path('user_info/',new_user_form_view,name='user_frm_req'),
path('n_upload_f/',new_upload_file_view,name='n_upload_f_req'),

]