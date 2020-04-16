from django.contrib import admin

from datatype.models import DataType


class DataTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'community', 'author', 'generic']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'name', 'community', 'created_on', 'author', 'generic')
    list_filter = ['author', 'community', 'generic']
    search_fields = ['name', 'community', 'author', 'generic']
    readonly_fields = ['created_on']


admin.site.register(DataType, DataTypeAdmin)
