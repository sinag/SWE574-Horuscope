from django.contrib.auth.models import User , AbstractUser
from django.db import models
from root import settings


class UserProfile(models.Model):

    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, default=settings.DEFAULT_ADMIN,
                                   blank=False, null=False, db_index=True)
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

