from django.contrib.auth.models import User
from django.db import models

# Create your models here.

def prod_prew_dir_path(instance:"Product",filename:str)->str:
    return f"products/prod_{instance.pk}/prev/{filename}"

class Product(models.Model):
    """
    В Модели содержатся товары для продажи
    Заказы тут: :model:`shop_app.Order`
    """
    class Meta:
        ordering=["name"]
        # db_table="tech_products"
        verbose_name_plural="Продукты "

    name=models.CharField(max_length=100)
    description=models.TextField(null=False,blank=True)
    price=models.DecimalField(default=0,max_digits=8,decimal_places=2)
    discount=models.SmallIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    arhive=models.BooleanField(default=False)
    preview=models.ImageField(null=True,blank=True,upload_to=prod_prew_dir_path)

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"

    @property
    def description_short(self):
        if len(self.description)<48:
            return  self.description
        else:
            return self.description[:48] + " ..."

def prod_img_dir_path(instance:"ProductImage",filename:str)->str:
    return f"products/prod_{instance.product.pk}/img/{filename}"

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image = models.ImageField(null=True, blank=True, upload_to=prod_img_dir_path)
    descriptions=models.CharField(max_length=200,null=False,blank=True)


class Order(models.Model):
    delivery_adress=models.TextField(null=True,blank=True)
    promocode=models.CharField(max_length=20,null=False,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    products=models.ManyToManyField(Product,related_name="orders")
    receipt=models.FileField(null=True,upload_to="orders/receipts")



