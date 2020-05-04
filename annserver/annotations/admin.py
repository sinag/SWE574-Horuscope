from django.contrib import admin

from annotations.models import Annotation


class AnnotationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['owner', 'created', 'data']})
    ]
    list_display = ('id', 'owner', 'created', 'data')
    list_filter = ['owner']
    readonly_fields = ['id', 'created']
    search_fields = ['owner']


admin.site.register(Annotation, AnnotationAdmin)
