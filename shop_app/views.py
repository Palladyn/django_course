from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import  HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from shop_app.forms import ProductForms,GroupForm
from shop_app.models import Product, Order


# Create your views here.
# def shop_index(request:HttpRequest):
#     print(request.path)
#     print(request.method)
#     print(request.headers)
#     return HttpResponse("<h1>Hello URAAA</h1>")

class n_shop_index(View):
    def get(self,request:HttpRequest):
        products = [
            ('laptop', 7999),
            ('nout', 76657),
            ('phone', 1822),
        ]

        context = {
            'name': "Palladyn",
            'products': products
        }
        return render(request, "shop_app/index.html", context=context)

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

class GListV(View):
    def get(self,request:HttpRequest):
        g = Group.objects.prefetch_related('permissions').all()

        context = {
            "groups": g,
            "form":GroupForm(),
        }
        return render(request, "shop_app/group_list.html", context=context)
    def post(self,request:HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
        # url = reverse("shop_app:group_list_n")
        # return redirect(url)
        return redirect(request.path)
        # return self.get(request)


@permission_required("shop_app.view_product",raise_exception=True)
def products_list(request:HttpRequest):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(request, "shop_app/products_list.html", context=context)

class ProListTW(TemplateView):
    template_name ="shop_app/products_list_n.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        products = Product.objects.all()
        context = {
            "products": products
        }
        return context

class ProListLW(ListView):
    template_name ="shop_app/products_list_n.html"
    # model=Product
    context_object_name = "products"
    queryset = Product.objects.filter(arhive=False)




class ProListV(View):
    def get(self,request:HttpRequest):
        products = Product.objects.all()
        context = {
            "products": products
        }
        return render(request, "shop_app/products_list_n.html", context=context)

class ProductDetV(View):
    def get(self,request:HttpRequest,pk:int):
        # pr=Product.objects.get(pk=pk)
        pr=get_object_or_404(Product,pk=pk)
        context = {
            "product": pr,
        }
        return render(request, "shop_app/det_prod.html", context=context)


class ProductLDV(DetailView):
    template_name = "shop_app/det_prod.html"
    model = Product
    pk_url_kwarg ="pk"
    context_object_name = "product"


@login_required
def order_list(request:HttpRequest):
    orders=Order.objects.select_related("user").prefetch_related("products").all()
    context={
        "orders":orders
    }
    return render(request, "shop_app/order_list_ols.html", context=context)

class OrderLW(LoginRequiredMixin,ListView):
    # template_name = "shop_app/order_list.html"
    queryset = Order.objects.select_related("user").prefetch_related("products")
    # model = Order
    # context_object_name = "orders"

class OrderDW(PermissionRequiredMixin,DetailView):
    permission_required = "shop_app.view_order"
    queryset = Order.objects.select_related("user").prefetch_related("products")




@user_passes_test(lambda self: True if self.request.user.username == "gena" else False,)
def create_new_product(request:HttpRequest):
    if request.method=="POST":
        form = ProductForms(request.POST)
        if form.is_valid():
            # name=form.cleaned_data["name"]
            # price=form.cleaned_data["price"]
            # description=form.cleaned_data["description"]
            # Product.objects.create(name=name,description=description,price=price)
            Product.objects.create(**form.cleaned_data)
            url = reverse("shop_app:product_list")
            return redirect(url)
    else:
        form = ProductForms()
    context={
        "form":form
            }

    return render(request, "shop_app/product_form_tmplate.html", context=context)

# class CreateProdV(UserPassesTestMixin,CreateView):
#     def test_func(self):
#         if self.request.user.username=="gena":
#             return True
#         return False
#
#     model = Product
#     fields = "name","description","price","discount"
#     success_url = reverse_lazy('shop_app:product_list_lw')
#
class CreateProdV(CreateView):
    model = Product
    fields = "name","description","price","discount"
    success_url = reverse_lazy('shop_app:product_list_lw')


class UpdeateProdV(UpdateView):
    model = Product
    fields = "name","description","price","discount"
    # success_url = reverse_lazy('shop_app:product_list_lw')
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse('shop_app:prod_det',kwargs={"pk":self.object.pk} )


class ProdDelV(DeleteView):
    model = Product
    # template_name = "shop_app/product_confrim_delete.html"
    success_url = reverse_lazy('shop_app:product_list_lw')

    def form_valid(self, form):
        success_url=self.get_success_url()
        self.object.arhive=True
        self.object.save()
        return HttpResponseRedirect(success_url)


















