"""
Tests for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalization_was_successful(self):
        """Test email normalization"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['TEST2@exAmple.com', 'test2@example.com'],
        ]

        for Entered_email, Expected_email in sample_emails:
            user = get_user_model().objects.create_user(Entered_email, 'sample123')
            self.assertEqual(user.email, Expected_email)

    def test_email_existence_for_each_user(self):
        """Test if user has provided any emails"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'smaple123')
