from django.contrib import admin

from integerfield.models import IntegerField


class IntegerFieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instance', 'property', 'value']}),
    ]
    list_display = ('id', 'instance', 'property', 'value')
    list_filter = ['instance', 'property']
    search_fields = ['instance', 'property']


admin.site.register(IntegerField, IntegerFieldAdmin)
