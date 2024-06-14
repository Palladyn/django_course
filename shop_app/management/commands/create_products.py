from django.core.management import BaseCommand
from shop_app.models import Product

class Command(BaseCommand):
    # Создание продуктов
    def handle(self, *args, **options):
        self.stdout.write("Создание Продукта")
        product_l=[
            "Laptop",
            "Desctop",
            "Notebook"
        ]
        for pn in product_l:
            pr,created=Product.objects.get_or_create(name=pn)
            self.stdout.write(f" Создан {pr.name}")
        self.stdout.write(self.style.SUCCESS("Продукт Создан"))

