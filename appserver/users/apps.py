from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from actstream import registry
        from comment.models import Comment
        from community.models import Community
        registry.register(self.get_model('CustomUser'))
        registry.register(Comment)
        registry.register(Community)

