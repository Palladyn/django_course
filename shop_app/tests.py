from string import ascii_letters
from random import choices

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from shop_app.models import Product
from shop_app.utils import plusP

# Create your tests here.
class PlusPTestCase(TestCase):
    def test_plusP(self):
        result=plusP(2,3)
        self.assertEqual(result,5)


class ProductCreateViewTestCase(TestCase):
    def setUp(self):
        self.product_name="".join(choices(ascii_letters,k=10))
        Product.objects.filter(name=self.product_name).delete()
    def test_product_create_view(self):
        response=self.client.post(reverse("shop_app:create_product_n"),
                         {"name":self.product_name,
                          "description":"oTrata",
                          "price":"1200.12",
                          "discount":"20"}
                         )
        self.assertRedirects(response,reverse('shop_app:product_list_lw'))
        self.assertTrue(Product.objects.filter(name=self.product_name).exists())

class ProductDetViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product=Product.objects.create(name="Bla_blaa_p")

    # def setUp(self) -> None:
    #     self.product=Product.objects.create(name="Bla_blaa_p")

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    # def tearDown(self) -> None:
    #     self.product.delete()

    def test_product_det_view1(self):
        response=self.client.get(reverse("shop_app:prod_det_pw",kwargs={"pk":self.product.pk}))
        self.assertEqual(response.status_code,200)

    def test_product_det_view2(self):
        response=self.client.get(reverse("shop_app:prod_det_pw",kwargs={"pk":self.product.pk}))
        self.assertContains(response,self.product.name)


class ProductsListViewTestCase(TestCase):
    fixtures = [
        'Products_data.json'
    ]

    def test_prod_list(self):
        response=self.client.get(reverse('shop_app:product_list_lw'))
        for prod in Product.objects.filter(arhive=False).all():
            self.assertContains(response,prod.name)

    def test_prod_list_1(self):
        response=self.client.get(reverse('shop_app:product_list_lw'))
        prods=Product.objects.filter(arhive=False).all()
        products_=response.context["products"]
        for p,p_ in zip(prods,products_):
            self.assertEqual(p.pk,p_.pk)

    def test_prod_list_2(self):
        response=self.client.get(reverse('shop_app:product_list_lw'))
        self.assertQuerysetEqual(
            qs=Product.objects.filter(arhive=False).all(),
            values=(p.pk for p in response.context["products"]),
            transform=lambda p:p.pk,
        )
        self.assertTemplateUsed(response,"shop_app/products_list_n.html")


class OrderLWTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.credentials=dict(username="gamaka",password="aqwsde123")
        cls.user=User.objects.create_user(**cls.credentials)
    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.login(**self.credentials)
#
    def test_orders_v(self):
        response=self.client.get(reverse('shop_app:order_list_lw'))
        # self.assertContains(response,"Orders")
        self.assertEqual(response.status_code,200)
