from django.template.response import TemplateResponse
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from . import models
import unittest

# Create your tests here.

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_1(self):
        response = self.client.get('/users/view/1/')
        self.assertEqual(response.status_code, 200)

    def test_2(self):
        response1 = self.client.get('/users/login/')
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.post('/users/login/', {'username': 'admin', 'password': 'admin'})
        self.assertEquals(response2.status_code,200)