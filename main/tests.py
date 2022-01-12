from django.http import response
from django.test import TestCase
from django.urls import reverse, resolve
from .views import home, about_us, contact_us 
# Create your tests here.

class ViewTestCase(TestCase):

    def test_home_view(self):
        res = resolve(reverse("home"))
        response = self.client.get(reverse("home"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Welcome to cherry")
        # self.assertEqual(response.content, b"Welcome To cherry homepage")
        self.assertEqual(res.func, home)
        self.assertTemplateUsed(response, 'home.html')

    def test_about_view(self):
        res = resolve(reverse("about"))
        response = self.client.get(reverse("about"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "About Us")
        # self.assertEqual(response.content, b"We sell cherry")
        self.assertEqual(res.func, about_us)
        self.assertTemplateUsed(response,'about.html')
    
    def test_contact_view(self):
        res = resolve(reverse("contact"))
        response = self.client.get(reverse("contact"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Contact Us")
        # self.assertEqual(response.content, b"This is our services")
        self.assertEqual(res.func, contact_us)
        self.assertTemplateUsed(response, 'contact.html')