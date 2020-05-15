from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    """Test case for user model"""

    def test_create_user_email_successful(self):
        """test creating a new user for model is successful"""
        email = 'test@gmial.com'
        password = 'testpassword123'
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_for_normalize_email(self):
        """test that the email is noramlize or not"""
        email = 'test@GAMAIL.COM'
        user = get_user_model().objects.create_user(email,'test')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """test if user doesnot write email"""
        # user = get_user_model().objects.create_user(None,'123')
        # self.assertRaises(ValueError)
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'123')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'teste@gmail.com','password123'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)