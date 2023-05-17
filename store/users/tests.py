from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.forms import UserRegistrationForm
# Create your tests here.
from users.models import *


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Valeriy',
            'last_name': 'Bondarchuk',
            'username': 'djok',
            'email': 'erasil@gmail.com',
            'password1': 'Hellowordl333',
            'password2': 'Hellowordl333',
        }
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        responce = self.client.get(self.path)

        self.assertEqual(responce.status_code, HTTPStatus.OK)
        self.assertEqual(responce.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(responce, 'users/register.html')

    def user_registration_post_success(self):

        responce = self.client.post(self.path, self.data)
        username = self.data['username']

        self.assertFalse(User.objects.filter(username=username).exists())

        # check creating user

        self.assertEqual(responce.status_code, HTTPStatus.FOUND)
        self.assertRedirects(responce, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        #check creating email verification

        email_verification = EmailVerification.objects.filter(username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(), now() + timedelta(hours=48).date()
        )

    def test_user_registration_post_error(self):
        user = User.objects.create(username=self.data['username'])
        responce = self.client.post(self.path, self.data)

        self.assertEqual(responce.status_code, HTTPStatus.OK)
        self.assertContains(responce, 'Пользователь с таким именем уже существует.', html=True)
