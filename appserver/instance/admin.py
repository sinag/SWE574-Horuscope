from django.contrib import admin

from instance.models import Instance


class InstanceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['author', 'datatype']}),
        ('Date information', {'fields': ['created_on', 'updated_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'author', 'created_on', 'updated_on', 'datatype')
    list_filter = ['datatype', 'author']
    search_fields = ['datatype', 'author']
    readonly_fields = ['created_on', 'updated_on']


admin.site.register(Instance, InstanceAdmin)
