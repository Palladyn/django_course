from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import GroupSerializer,ProductSerializer

# Create your views here.
@api_view()
def hello_w_view(request:Request)->Response:
    return Response({"message":"Hello Chuwak"})

class GroupsListView(APIView):
    def get(self,request:Request )->Response:
        gr=Group.objects.all()
        data=[group.name for group in gr]
        return Response({"group":data})

class GroupsListViewS(APIView):
    def get(self,request:Request )->Response:
        gr=Group.objects.all()
        serializer=GroupSerializer(gr,many=True)
        return Response({"group":serializer.data})

class GroupsListViewSM(ListModelMixin,GenericAPIView):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer

    def get(self,request:Request )->Response:
        return self.list(request)


class GroupsListViewSLM(ListCreateAPIView):
    queryset=Group.objects.all()
    serializer_class=GroupSerializer



class ProdViewSet(ModelViewSet):
    """
    Набор для действий над продуктами
    """
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields=["name","description"]
    filterset_fields=[
        "name","description","price","discount","arhive"
    ]
    ordering_fields=[
        "name", "description", "price", "discount", "arhive"
    ]



