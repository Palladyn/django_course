from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shop_app.models import  Order


class Command(BaseCommand):
    # Создание продуктов
    def handle(self, *args, **options):
        self.stdout.write("Создание Заказа")
        user=User.objects.get(username="palladyn")
        order=Order.objects.get_or_create(
            delivery_adress="Ul. Komarova dom 3",
            promocode="xs97828",
            user=user
        )
        self.stdout.write(f" Заказа {order}")
        self.stdout.write(self.style.SUCCESS("Заказ Создан"))

