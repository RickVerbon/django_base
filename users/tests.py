from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(
            username="Batman",
            password="batman123",
            email="brunce@wayneenterprises.com",
            first_name="Bruce",
            last_name="Wayne")

    def test_user_exists(self):
        batman = User.objects.get(username="Batman")
        self.assertEqual(batman.first_name, "Bruce")
        self.assertEqual(batman.email, "brunce@wayneenterprises.com")

    def test_user_does_not_exist(self):
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username="Superman")
