from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse, path
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin

from instance.models import Instance
from .models import UserProfile


class CreateView(CreateView):
    model = UserProfile
    fields = []
    template_name = 'userprofile/index.html'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_name'] = Instance.objects.all().filter(id=self.kwargs.get('id')).first()
        print("get_context_data runs")
        print(context['user_name'])
        return context

    def form_valid(self, form):
        """
        Assign comment data inside a transaction object
        """
        with transaction.atomic():
            form.instance.created_by = self.request.user
            form.instance.instance = Instance.objects.all().filter(id=self.kwargs.get('instance_id')).first()
            form.instance.save()
            return FormMixin.form_valid(self, form)

    def get_success_url(self):
        instance_id = self.kwargs.get('instance_id')
        return reverse('userprofile:profile_page', args=(instance_id,))

