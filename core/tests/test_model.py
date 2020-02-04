from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successfull(self):
        """ test creating a new user with email its successfull"""
        email = 'test@gmail.com'
        password = 'test1234'
        user = get_user_model().objects.create_user(
            email= email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))