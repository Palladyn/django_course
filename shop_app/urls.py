from django.urls import path

from shop_app.views import shop_index

app_name="shop_app"

urlpatterns = [
path('',shop_index,name='index_shop')
]
