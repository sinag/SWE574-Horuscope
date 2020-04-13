from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from community.models import Community
from .models import Subscription

"""
Class based view to create new subscription
"""


class CreateView(CreateView):
    model = Subscription
    fields = []
    template_name = 'subscription/create.html'

    def query_community(self):
        return Community.objects.all().filter(id=self.kwargs.get('pk')).get()

    def get_context_data(self, **kwargs):
        ctx = super(CreateView, self).get_context_data(**kwargs)
        ctx['community'] = self.query_community()
        return ctx

    def form_valid(self, form):
        """
        Assign subscription data
        """
        form.instance.user = self.request.user
        form.instance.community = Community.objects.all().filter(id=self.kwargs.get('pk')).get()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:index')


"""
Class based view to remove existing subscription
"""


class DeleteView(DeleteView):
    model = Subscription
    template_name = 'subscription/delete.html'
    success_url = reverse_lazy('community:index')

    def get_success_url(self):
        return reverse('community:index')

    def get_queryset(self):
        """
        Get subscription details to remove
        """
        return Subscription.objects.filter(id=self.kwargs.get('pk'))
