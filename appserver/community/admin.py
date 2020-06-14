from django.contrib import admin
from .models import Community


class CommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'author', 'city']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'created_on', 'author', 'city')
    list_filter = ['name', 'author']
    search_fields = ['name', 'author']


admin.site.register(Community, CommunityAdmin)
