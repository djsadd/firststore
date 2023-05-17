from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import *


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Главная')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductListViewTestCase(TestCase):
    fixtures = ['categories.json', 'goods.json']

    def setUP(self):
        self.products = Product.objects.all()
    def test_list(self):
        path = reverse('products:index')
        responce = self.client.get(path)

        self._commot_test(responce)
        self.assertEqual(list(responce.context_data['object_list']), list(self.products[:3]))

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={"category_id": category.id})
        responce = self.client.get(path)

        self._commot_test(responce)
        self.assertEqual(
            list(responce.context_data['object_list']), list(self.products.filter(category_id=category.id)[:3])
        )

    def _commot_test(self, responce):
        self.assertEqual(responce.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(responce, 'products/products.html')
        self.assertEqual(responce.context_data['title'], 'Store - Каталог')