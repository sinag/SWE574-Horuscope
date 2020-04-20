from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin

from instance.models import Instance
from .models import Flag

"""
Class based view to create new flag
"""


class CreateView(CreateView):
    model = Flag
    fields = ['description']
    template_name = 'flag/create.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['instance'] = Instance.objects.all().filter(id=self.kwargs.get('instance_id')).get()
        return context

    def form_valid(self, form):
        """
        Assign flag data inside a transaction object
        """
        with transaction.atomic():
            form.instance.created_by = self.request.user
            form.instance.instance = Instance.objects.all().filter(id=self.kwargs.get('instance_id')).first()
            form.instance.save()
            return FormMixin.form_valid(self, form)

    def get_success_url(self):
        return reverse('community:index')


"""
Class based view to delete existing flag
"""


class DeleteView(DeleteView):
    model = Flag
    template_name = 'flag/delete.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        instance_id = Flag.objects.filter(id=self.kwargs.get('pk')).first().instance_id
        context['instance'] = Instance.objects.all().filter(id=instance_id).get()
        return context

    def get_success_url(self):
        return reverse('community:index')

    def get_queryset(self):
        """
        Get community details to delete
        """
        return Flag.objects.filter(id=self.kwargs.get('pk'))
