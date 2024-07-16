from django.contrib import admin

from my_api_app.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name','description_short','price','discount','created_at','arhive']
    list_display_links = ['name',]
    ordering=["pk",]
    search_fields=["name","description"]

