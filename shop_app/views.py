from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
# def shop_index(request:HttpRequest):
#     print(request.path)
#     print(request.method)
#     print(request.headers)
#     return HttpResponse("<h1>Hello URAAA</h1>")

def shop_index(request:HttpRequest):
    products=[
        ('laptop', 7999),
        ('nout', 76657),
        ('phone', 1822),
    ]

    context={
        'name':"Palladyn",
        'products':products
    }
    return render(request,"shop_app/index.html",context=context)


def show_group_list(request:HttpRequest):
    g=Group.objects.prefetch_related('permissions').all()

    context={
        "groups":g
    }
    return render(request,"shop_app/group_list.html",context=context)