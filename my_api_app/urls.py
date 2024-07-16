from django.urls import path,include
from rest_framework.routers import DefaultRouter

from my_api_app.views import hello_w_view,GroupsListView,GroupsListViewS,GroupsListViewSM,GroupsListViewSLM,ProdViewSet

app_name="my_api_app"
router=DefaultRouter()
router.register("products",ProdViewSet)
urlpatterns = [
    path('hello/',hello_w_view,name='hello'),
    path('grs/',GroupsListView.as_view(),name='groups'),
    path('grsS/',GroupsListViewS.as_view(),name='groupsS'),
    path('grsSM/',GroupsListViewSM.as_view(),name='groupsSM'),
    path('grsSLM/',GroupsListViewSLM.as_view(),name='groupsSLM'),
    path('ProdVS/',include(router.urls)),

]