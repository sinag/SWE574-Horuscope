from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from community.models import Community
from datatype.models import DataType


def create_test_user(name, password):
    """
    Create a test user with given parameters
    """
    return get_user_model().objects.create_user(username=name, password=password)


def create_community(name, description, user):
    """
    Create a community with given parameters
    """
    return Community.objects.create(name=name, description=description, author=user)


def create_datatype(community, author, name, description):
    """
    Create a datatype with given parameters
    """
    return DataType.objects.create(name=name, description=description, author=author, community=community, generic=1)


class DataTypeIndexViewTests(TestCase):
    def test_no_datatype(self):
        """
        If no datatype exists, an appropriate message is displayed.
        """
        user = create_test_user("test_user", "Passw0rd1")
        community = create_community(name="Test Community Name", description="Test Community Description", user=user)
        response = self.client.get(reverse('datatype:index', kwargs={'community_id': community.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oops, no post type found!")
        self.assertQuerysetEqual(response.context['datatypes'], [])

    def test_datatype_list(self):
        """
        Communities shall be displayed on the index page.
        Create a test user, create a test community with this user and try to view test community from
        community index page
        """
        user = create_test_user("test_user", "Passw0rd1")
        community = create_community(name="Test Community Name", description="Test Community Description", user=user)
        create_datatype(community, user, "Test DataType Name", "Tes DataType Description")
        response = self.client.get(reverse('datatype:index', kwargs={'community_id': community.id}))
        self.assertQuerysetEqual(
            response.context['datatypes'],
            ['<DataType: 1-Test DataType Name>']
        )
