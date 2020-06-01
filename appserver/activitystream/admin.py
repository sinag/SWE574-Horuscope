from django.contrib import admin

from activitystream.models import ActivityStream


class ActivityStreamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['created', 'data']})
    ]
    list_display = ('id', 'created', 'data')
    readonly_fields = ['id', 'created']


admin.site.register(ActivityStream, ActivityStreamAdmin)
