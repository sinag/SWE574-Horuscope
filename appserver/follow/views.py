from django.db import transaction
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from instance.models import Instance
from users.models import CustomUser
from .models import Follow

"""
Class based view to create new flag
"""


class CreateView(CreateView):
    model = Follow
    fields = []
    template_name = 'follow/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['target'] = CustomUser.objects.all().filter(id=self.kwargs.get('target_id')).first()
        return context

    def form_valid(self, form):
        """
        Assign flag data inside a transaction object
        """
        with transaction.atomic():
            form.instance.source = self.request.user
            form.instance.target = CustomUser.objects.all().filter(id=self.kwargs.get('target_id')).first()
            form.instance.save()
            return FormMixin.form_valid(self, form)

    def get_success_url(self):
        return reverse('activitystream:index')


"""
Class based view to delete existing flag
"""


class DeleteView(DeleteView):
    model = Follow
    template_name = 'follow/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        follow = Follow.objects.filter(id=self.kwargs.get('pk')).first()
        context['follow'] = follow
        return context

    def get_success_url(self):
        return reverse('activitystream:index')

    def get_queryset(self):
        """
        Get follow details to delete
        """
        return Follow.objects.filter(id=self.kwargs.get('pk'))
