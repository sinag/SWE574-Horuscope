from django.contrib import admin

from datetimefield.models import DateTimeField


class DateTimeFieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instance', 'property', 'value']}),
    ]
    list_display = ('id', 'instance', 'property', 'value')
    list_filter = ['instance', 'property']
    search_fields = ['instance', 'property']


admin.site.register(DateTimeField, DateTimeFieldAdmin)
