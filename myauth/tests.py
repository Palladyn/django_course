from django.test import TestCase
from django.urls import reverse
import json
# Create your tests here.
class GetCookieViewTestCase(TestCase):
    def test_get_cookie_view(self):
        response=self.client.get(reverse('myauth:get_c'))
        self.assertContains(response,"Cookie value")

class FromTestViewTestCase(TestCase):
    def test_from_test_view(self):
        response=self.client.get(reverse('myauth:tst_json'))
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.headers['content-type'],'application/json')
        excepted_data={"foo":"bar","spam":"eggs"}
        # r_d=json.loads(response.content)
        # self.assertEqual(r_d,excepted_data)
        self.assertJSONEqual(response.content,excepted_data)
        self.assertContains(response, "spam")

