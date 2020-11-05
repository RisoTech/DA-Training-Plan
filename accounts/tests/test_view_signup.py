from ..forms import SignUpForm
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import signup
# Create your tests here.

class SignUpTests(TestCase):

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_sign_up_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_resolves_sign_up_view(self):
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')
    
    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, SignUpForm)
    
    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)

    
class SuccessfullSignUpTests(TestCase):

    def setUp(self):
        data = {
            'username':'donga2607',
            'email':'donga.ftu2@gmail.com',
            'password1':'abcdef123456',
            'password2':'abcdef123456',
        }
        url = reverse('signup')
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        # Test redirect after signup
        self.assertRedirects(self.response, self.home_url)
    
    def test_successfull_sign_up(self):
        self.assertTrue(User.objects.exists())
    
    def test_user_authentication(self):
        response = self.client.get(reverse('home'))
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignUpTest(TestCase):
    
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})
    
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)
     
    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
    
    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())


















