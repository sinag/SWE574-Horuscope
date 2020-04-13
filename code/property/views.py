from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, DeleteView

from datatype.models import DataType
from property.models import Property

"""
Class based index view to list properties of a community
"""


class IndexView(generic.ListView):
    template_name = 'property/index.html'
    context_object_name = 'properties'

    def get_queryset(self):
        """
        Get property list sorted by creation date
        """
        return Property.objects.all().filter(datatype__id=self.kwargs.get('datatype_id')).order_by('created_on')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


"""
Class based view to create new property
"""


class CreateView(CreateView):
    model = Property
    fields = ['name', 'type', 'required']
    template_name = 'property/create.html'

    def form_valid(self, form):
        """
        Assign property data
        """
        form.instance.author = self.request.user
        form.instance.generic = False
        form.instance.datatype = DataType.objects.get(id=self.kwargs.get('datatype_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('property:index', kwargs={'datatype_id': self.kwargs.get('datatype_id')})


"""
Class based view to delete existing property
"""


class DeleteView(DeleteView):
    model = Property
    template_name = 'property/delete.html'

    def get_success_url(self):
        return reverse('property:index', kwargs={'datatype_id': self.kwargs.get('datatype_id')})

    def get_queryset(self):
        """
        Get property details to delete
        """
        return Property.objects.filter(id=self.kwargs.get('pk'))
