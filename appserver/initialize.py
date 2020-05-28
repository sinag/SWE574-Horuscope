import django

django.setup()

from django.contrib.auth import get_user_model
from community.models import Community

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    Community(name="Test Community Name", description="Test Community Description").save()
