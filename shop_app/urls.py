from django.urls import path

from shop_app.views import shop_index,show_group_list,products_list,order_list,create_new_product,n_shop_index,\
    GListV,ProListV,ProductDetV,ProListTW,ProListLW,ProductLDV,OrderLW,OrderDW,CreateProdV,UpdeateProdV,ProdDelV

app_name="shop_app"

urlpatterns = [
    path('old/',shop_index,name='index_shop'),
    path('',n_shop_index.as_view(),name='index_shop'),
    path('show_group/',show_group_list,name='group_list'),
    path('show_group_n/',GListV.as_view(),name='group_list_n'),
    path('show_product_list/',products_list,name='product_list'),
    path('show_product_list_tw/',ProListTW.as_view(),name='product_list_tw'),
    path('show_product_list_lw/',ProListLW.as_view(),name='product_list_lw'),
    path('show_product_list_n/',ProListV.as_view(),name='product_list_n'),
    path('show_det_p/<int:pk>',ProductDetV.as_view(),name='prod_det'),
    path('show_det_pw/<int:pk>', ProductLDV.as_view(), name='prod_det_pw'),
    path('show_order_list/',order_list,name='order_list'),
    path('show_order_list_lw/',OrderLW.as_view(),name='order_list_lw'),
    path('show_order_det/<int:pk>',OrderDW.as_view(),name='order_dw'),
    path('create_p/',create_new_product,name='create_product'),
    path('create_p_n/',CreateProdV.as_view(),name='create_product_n'),
    path('update_p_n/<int:pk>',UpdeateProdV.as_view(),name='update_product_n'),
    path('delete_p_n/<int:pk>',ProdDelV.as_view(),name='delete_product_n'),
]
