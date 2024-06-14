from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=False,blank=True)
    price=models.DecimalField(default=0,max_digits=8,decimal_places=2)
    discount=models.SmallIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    arhive=models.BooleanField(default=False)
