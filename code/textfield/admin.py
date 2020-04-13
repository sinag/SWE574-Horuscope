from django.contrib import admin

from textfield.models import TextField


class TextFieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['instance', 'property', 'value']}),
    ]
    list_display = ('id', 'instance', 'property', 'value')
    list_filter = ['instance', 'property']
    search_fields = ['instance', 'property']


admin.site.register(TextField, TextFieldAdmin)
