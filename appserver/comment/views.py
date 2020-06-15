from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse, path
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin

from instance.models import Instance
from .models import Comment

"""
Class based view to create new comment
"""


class CreateView(CreateView):
    model = Comment
    fields = ['body']
    template_name = 'comment/create.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['instance'] = Instance.objects.all().filter(id=self.kwargs.get('instance_id')).get()
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
        return reverse('comment:comments', args=(instance_id,))


"""
Class based view to update existing comment
"""


class UpdateView(UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'comment/update.html'

    def get_success_url(self):
        instance_id = Comment.objects.filter(id=self.kwargs.get('pk')).first().instance_id
        return reverse('comment:comments', args=(instance_id,))

    def get_queryset(self):
        """
        Get comment details to update
        """
        return Comment.objects.filter(id=self.kwargs.get('pk'))


"""
Class based view to delete existing comment
"""


class DeleteView(DeleteView):
    model = Comment
    template_name = 'comment/delete.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        instance_id = Comment.objects.filter(id=self.kwargs.get('pk')).first().instance_id
        context['instance'] = Instance.objects.all().filter(id=instance_id).get()
        return context

    def get_success_url(self):
        instance_id = Comment.objects.filter(id=self.kwargs.get('pk')).first().instance_id
        return reverse('comment:comments', args=(instance_id,))

    def get_queryset(self):
        """
        Get comment details to delete
        """
        return Comment.objects.filter(id=self.kwargs.get('pk'))


class CommentsView(generic.ListView):
    model = Instance
    template_name = 'comment/list.html'
    context_object_name = 'comments'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['instance'] = Instance.objects.all().filter(id=self.kwargs.get('instance_id')).get()
        return context

    def get_queryset(self):
        """
        Get comment details
        """
        return (
            Comment.objects
                .select_related('created_by')
                .filter(instance_id=self.kwargs.get('instance_id')).order_by('-created_on')
        )
