from django.db import models


class Annotation(models.Model):
    owner = models.ForeignKey('auth.User', related_name='annotations', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    data = models.TextField()

    class Meta:
        ordering = ['created']
        verbose_name = "annotation"
        verbose_name_plural = "annotations"
