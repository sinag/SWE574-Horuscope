import django

django.setup()

from django.contrib.auth import get_user_model
from annotations.models import Annotation

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    # Annotation(owner_id=1, data="{\"@context\": \"http://www.w3.org/ns/anno.jsonld\",\"id\": "
    #                             "\"http://example.org/anno1\",\"type\": \"Annotation\",\"body\": "
    #                             "\"http://example.org/post1\",\"target\": \"http://example.com/page1\"}").save()
