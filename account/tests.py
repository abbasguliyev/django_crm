from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

class UserTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(email="test@example.com", password="TestPassword@123")
        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()

    def test_get_user(self):
        self.assertEqual(self.user.email, "test@example.com")

    def test_update_user(self):
        self.user.email = "test2@example.com"
        self.user.save()
        self.assertEqual(self.user.email, "test2@example.com")