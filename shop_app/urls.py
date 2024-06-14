from django.urls import path

from shop_app.views import shop_index,show_group_list

app_name="shop_app"

urlpatterns = [
    path('',shop_index,name='index_shop'),
    path('show_group/',show_group_list,name='group_list')
]
