from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from community.models import Community


def create_test_user(name, password):
    """
    Create a test user with given parameters
    """
    return get_user_model().objects.create_user(username=name, password=password)


def create_community(author, name, description):
    """
    Create a community with given parameters
    """
    return Community.objects.create(name=name, description=description, author=author)


class CommunityIndexViewTests(TestCase):
    def test_no_community(self):
        """
        If no community exists, an appropriate message is displayed.
        """
        response = self.client.get(reverse('community:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Oops, no community found!")
        self.assertQuerysetEqual(response.context['communities'], [])

    def test_community_list(self):
        """
        Communities shall be displayed on the index page.
        Create a test user, create a test community with this user and try to view test community from
        community index page
        """
        user = create_test_user("test_user", "Passw0rd1")
        create_community(name="Test Community Name", description="Test Community Description", user=user)
        response = self.client.get(reverse('community:index'))
        self.assertQuerysetEqual(
            response.context['communities'],
            ['<Community: Test Community Name>']
        )
