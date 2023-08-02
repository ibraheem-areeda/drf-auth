# from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# settings.configure()
from rest_framework.test import APITestCase
from rest_framework import status
from items.models import Item

print(Item)

class ItemTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save() 

    

        test_item = Item.objects.create(
            name="tst",
            purcheser=testuser1,
            price="120",
        )
        test_item.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")  


    def test_items_model(self):
        print(Item.objects.get(id =1))
        item = Item.objects.get(id=1)
        actual_purcheser = str(item.purcheser)
        actual_name = str(item.name)
        actual_price = str(item.price)
        self.assertEqual(actual_purcheser, "testuser1")
        self.assertEqual(actual_name, "tst")
        self.assertEqual(
            actual_price,"120"
        )

    def test_get_item_list(self):
        url = reverse("item_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        items = response.data
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["name"], "tst")


    def test_auth_required(self):
        self.client.logout() 
        url = reverse("item_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete_thing(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("item_detail",args=[1])  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)