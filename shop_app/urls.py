from django.urls import path

from shop_app.views import shop_index,show_group_list,products_list,order_list

app_name="shop_app"

urlpatterns = [
    path('',shop_index,name='index_shop'),
    path('show_group/',show_group_list,name='group_list'),
    path('show_product_list/',products_list,name='product_list'),
    path('show_order_list/',order_list,name='order_list'),
]
