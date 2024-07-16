from django.db import models

# Create your models here.

def prod_prew_dir_path(instance:"Product",filename:str)->str:
    return f"products/api_prod_{instance.pk}/prev/{filename}"

class Product(models.Model):
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