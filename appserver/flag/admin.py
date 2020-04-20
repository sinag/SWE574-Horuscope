from django.contrib import admin

from flag.models import Flag


class FlagAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instance', 'created_by', 'description']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'instance', 'created_by', 'created_on', 'description')
    list_filter = ['instance', 'created_by']
    search_fields = ['instance', 'created_by']
    readonly_fields = ['created_on']


admin.site.register(Flag, FlagAdmin)