from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shop_app.models import Order, Product


class Command(BaseCommand):
    # Создание продуктов
    def handle(self, *args, **options):
        self.stdout.write("Обновление Заказа")
        order=Order.objects.first()
        if not order:
            self.stdout.write(f"Нет Заказов")
            return
        else:
            products=Product.objects.all()
            for p in products:
                order.products.add(p)
        self.stdout.write(self.style.SUCCESS("Заказ Обновлен"))

