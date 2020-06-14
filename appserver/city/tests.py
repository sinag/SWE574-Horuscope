import datetime
from datetime import date

from django.template.response import TemplateResponse
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from community.models import Community
from django.urls import reverse

from . import views
from . import models
import unittest
from users.models import CustomUser


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        user = CustomUser(first_name="Tester", last_name="1", email="test@test.com")
        user.save()
        community = Community(author=user, name="Test Community", created_on = datetime.datetime.now(), description = "Hi Test")
        community.save()
        self.community = community


    def test_city(self):
        pk = self.community.pk
        response1 = self.client.get('/city/'+ str(pk) + '/')
        self.assertEqual(response1.status_code, 200)
        response2 = self.client.post('/city/1/', {'q': "Ankara"})
        self.assertEqual(response2.status_code, 200)