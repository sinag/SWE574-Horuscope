from django.contrib import admin

from comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instance', 'created_by', 'body']}),
        ('Date information', {'fields': ['created_on'], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'instance', 'created_by', 'created_on', 'body')
    list_filter = ['instance', 'created_by']
    search_fields = ['instance', 'created_by']
    readonly_fields = ['created_on']


admin.site.register(Comment, CommentAdmin)