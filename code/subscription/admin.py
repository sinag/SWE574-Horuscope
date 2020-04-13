from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'community']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'user', 'community', 'created_on')
    list_filter = ['user', 'community']
    search_fields = ['user', 'community']
    readonly_fields = ['created_on']


admin.site.register(Subscription, SubscriptionAdmin)
