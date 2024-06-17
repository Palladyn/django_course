from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
# Create your views here.

def process_get_view(request:HttpRequest):
    a=request.GET.get("a"," ")
    b=request.GET.get("b"," ")
    result=a+b
    context={
        'a': a,
        'b': b,
        'result': result
    }
    return render(request, "requestapp/request-query-params.html", context=context)

def user_form_view(request:HttpRequest):
    context = {

    }
    return render(request, "requestapp/user-form.html", context=context)


def upload_file_view(request:HttpRequest):
    if request.method=="POST" and request.FILES.get("myfile"):
        myfile=request.FILES["myfile"]
        fs=FileSystemStorage()
        fil_n=fs.save(myfile.name,myfile)
        print(f"Файл Сохранен {fil_n}")
    context = {

    }
    return render(request, "requestapp/file-upload.html", context=context)