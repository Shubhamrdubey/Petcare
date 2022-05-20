from urllib import response
from django.test import SimpleTestCase,TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class Testhome(SimpleTestCase):

    def test_home_status(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)

    def test_home_name(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_template(self):
        response=self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'home.html')

class Testsignup(TestCase):

    def test_url(self):
        response=self.client.get('/users/signup/')
        self.assertEqual(response.status_code,200)
    
    def test_url_name(self):
        response=self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)

    def test_template(self):
        response=self.client.get(reverse('signup'))
        self.assertTemplateUsed(response,'signup.html')

    username='testuser'
    email='a@b.com'

    def test_signup(self):
        p=get_user_model()
        new_user=p.objects.create_user(self.username,self.email)
        self.assertEqual(p.objects.all().count(),1)
        self.assertEqual(p.objects.all()[0].username,self.username)
        self.assertEqual(p.objects.all()[0].email,self.email)
