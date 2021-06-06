from django.http import response
from django.test import TestCase
from rest_framework.test import APITestCase
from main.models import Product
from django.urls import reverse
from rest_framework import status



class TestCreateProduct(TestCase):

    @classmethod
    def setUpTestData(cls):

        test_product = Product.objects.create(name="product",
            description="description", price=150)
        
    def test_product_content(self):

        product = Product.objects.get(id=1)
        name = f'{product.name}'
        description = f'{product.description}'
        price = f'{product.price}'
        slug = f'{product.slug}'
        active = f'{product.active}'
        in_stock = f'{product.in_stock}'

        self.assertEqual(name, 'product')
        self.assertEqual(description, 'description')
        self.assertEqual(price, '150.00')
        self.assertEqual(slug, 'product')
        self.assertEqual(active, 'True')
        self.assertEqual(in_stock, 'True')
        self.assertEqual(str(product), 'product')


class PostTest(APITestCase):

    def test_view_post(self):

        url = reverse('product-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):

        data = {
            "name": "new name",
            "description": "new description",
            "price": 150,
            }
        url = reverse('product-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    



