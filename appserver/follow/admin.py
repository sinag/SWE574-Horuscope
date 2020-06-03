from django.contrib import admin

from follow.models import Follow


class FollowAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['source', 'target']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'source', 'target', 'created_on')
    list_filter = ['source', 'target']
    search_fields = ['source', 'target']
    readonly_fields = ['created_on']


admin.site.register(Follow, FollowAdmin)