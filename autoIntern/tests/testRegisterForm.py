"""Tests the forms on the website"""
from autoIntern.models import User
from django.test import TestCase
from autoIntern.forms import UserForm

class RegisterFormTest(TestCase):
    def setUp(self):
        pass

    def test_valid_data(self):
        form = UserForm({
            'email' : 'test',
            'displayName': 'test',
            'firstName': 'test',
            'lastName': 'test',
            'group': 'test',
            'password': 'test',
            'title': 'test'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_data(self):
        form = UserForm({
            'displayName': 'test',
            'firstName': 'test',
            'lastName': 'test',
            'group': 'test',
            'password': 'test',
            'title': 'test'
        })
        self.assertFalse(form.is_valid())

    def test_home_view(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'autoIntern/homePage.html')

    def test_register_user_form_view(self):
        user_count = User.objects.count()
        response = self.client.post("/register/", {
            'email' : 'test',
            'displayName': 'test',
            'firstName': 'test',
            'lastName': 'test',
            'group': 'test',
            'password': 'test',
            'title': 'test'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertTrue(', test' in str(response.content))

    def test_user_login_view(self):
        user = User(email = 'test',
            displayName = 'test',
            firstName = 'test',
            lastName = 'test',
            group = 'test',
            password = 'test',
            title = 'test')
        user.save()
        self.assertIsNotNone(User.objects.get(email='test'))
        response = self.client.post("/login/", {
            'email' : 'test',
            'password' : 'test'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Hello' in str(response.content))

    def test_user_upload_view(self):
        # @Dom fill this in as I did above when you get here
        self.assertTrue(True)