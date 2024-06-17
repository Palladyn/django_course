from django.contrib import admin
from django.http import HttpRequest
from django.db.models import QuerySet

from .admin_mixin import ExportAsCSVMixin
from  .models import Product,Order

# Register your models here.

class OrderInline(admin.TabularInline):
    model = Product.orders.through

@admin.action(description="Архивировать")
def mark_arhived(modeladmin:admin.ModelAdmin,request:HttpRequest,queryset:QuerySet):
    queryset.update(arhive=True)


@admin.action(description="Разархивировать")
def mark_dearhived(modeladmin:admin.ModelAdmin,request:HttpRequest,queryset:QuerySet):
    queryset.update(arhive=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin,ExportAsCSVMixin):
    actions = [
        mark_arhived,
        mark_dearhived,
        "export_csv",
    ]
    inlines = [
        OrderInline
    ]
    list_display = ['name','description_short','price','discount','created_at','arhive']
    list_display_links = ['name',]
    ordering=["pk",]
    search_fields=["name","description"]
    fieldsets = [
        (None,{
            "fields":("name","description")
        }),
    ("Price options",{
            "fields":("price","discount"),
            "classes":("collapse",),
        }),
    ("Extra options",{
            "fields":("arhive",),
            "classes":("collapse",),
            "description": "Extra options. Field 'arhived' is soft delated"
        }),

    ]

# admin.site.register(Product,ProductAdmin)

class ProductInline(admin.TabularInline):
    model=Order.products.through

# class ProductInline(admin.StackedInline):
#     model=Order.products.through
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=[
        ProductInline,
            ]
    list_display=['delivery_adress','promocode','created_at','user_verbose',]

    def get_queryset(self, request):
        return  Order.objects.select_related("user").prefetch_related("products")

    def user_verbose(self,obj:Order):
        return obj.user.first_name or obj.user.username
