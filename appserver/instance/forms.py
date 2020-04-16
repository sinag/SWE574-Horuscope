from django import forms


class DynamicPost(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DynamicPost, self).__init__(*args, **kwargs)


