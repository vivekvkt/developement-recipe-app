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
        
    def test_new_user_email_normalized(self):
        """ test new user email normlized """
        email  = 'hello@GMAIL.COM'
        user = get_user_model().objects.create_user(email,'test1234')
        
        self.assertEqual(user.email, email.lower())
        
    
    def test_new_user_invalid_email(self):
        """ test creating user with no email erro """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')
            
            
    def test_create_new_superuser(self):
        """ test creating new superuser """
        user = get_user_model().objects.create_superuser(
            'hello@gmail.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)