from django.db import transaction
from django.urls import reverse
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin, FormView

from datetimefield.models import DateTimeField
from instance.models import Instance
from integerfield.models import IntegerField
from property.models import Property
from textfield.models import TextField
from .forms import SearchForm
from .models import DataType
from community.models import Community

"""
Class based index view to list datatypes inside a community
"""


class IndexView(generic.ListView):
    template_name = 'datatype/index.html'
    context_object_name = 'datatypes'

    def get_queryset(self):
        """
        Get datatype list from community sorted by creation date
        """
        return DataType.objects.all().filter(community__id=self.kwargs.get('community_id')).order_by(
            'generic').order_by('created_on')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


"""
Class based view to create new datatype
"""


class CreateView(CreateView):
    model = DataType
    fields = ['name', 'description']
    template_name = 'datatype/create.html'

    def form_valid(self, form):
        """
        Assign datatype data inside a transaction object
        """
        with transaction.atomic():
            form.instance.author = self.request.user
            form.instance.generic = False
            form.instance.community = Community.objects.get(id=self.kwargs.get('community_id'))
            form.instance.save()
            property_title = Property(datatype=form.instance, author=self.request.user, name='Title', type=0, generic=1,
                                      required=True)
            property_title.save()
            property_semantic_tag = Property(datatype=form.instance, author=self.request.user, name='Semantic Tags',
                                             type=0, generic=1, required=True)
            property_semantic_tag.save()
            return FormMixin.form_valid(self, form)

    def get_success_url(self):
        return reverse('datatype:index', kwargs={'community_id': self.kwargs.get('community_id')})


"""
Class based view to delete existing datatype
"""


class DeleteView(DeleteView):
    model = DataType
    template_name = 'datatype/delete.html'

    def get_success_url(self):
        return reverse('datatype:index', kwargs={'community_id': self.kwargs.get('community_id')})

    def get_queryset(self):
        """
        Get datatype details to delete
        """
        return DataType.objects.filter(id=self.kwargs.get('pk'))


"""
Class based view to update existing datatype
"""


class UpdateView(UpdateView):
    model = DataType
    fields = ['name', 'description']
    template_name = 'datatype/update.html'

    def get_success_url(self):
        return reverse('datatype:index', kwargs={'community_id': self.kwargs.get('community_id')})

    def get_queryset(self):
        """
        Get datatype details to update
        """
        return DataType.objects.filter(id=self.kwargs.get('pk'))


"""
Class based view to search using datatype
"""


class SearchView(FormView):
    template_name = 'datatype/search.html'
    form_class = SearchForm

    def form_valid(self, form):
        self.request.session['search_data'] = form.data
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('datatype:result', kwargs={'community_id': self.kwargs.get('community_id'),
                                                  'datatype_id': self.kwargs.get('datatype_id')})


"""
Class based view to show search results using datatype
"""


class ResultView(generic.ListView):
    model = Instance
    template_name = 'datatype/results.html'
    context_object_name = 'instances'

    def get_queryset(self):
        """
        Get search results
        Create a list for serach results, which contains instance_id's for results
        """
        search_results = []
        search_keywords = []
        search_data = self.request.session.get('search_data')
        for field in DataType.objects.get(id=self.kwargs.get('datatype_id')).fields():
            if search_data[field.name] is not '':
                search_keywords.append(search_data[field.name])

        for instance in Instance.objects.filter(datatype_id=self.kwargs.get('datatype_id')):
            instance_id = instance.id
            search_match = []
            for field in DataType.objects.get(id=self.kwargs.get('datatype_id')).fields():
                search_keyword = search_data[field.name]
                if field.type == 0 or field.type == 4 or field.type == 5 or field.type == 6 or field.type == 7 or field.type == 8 or field.type == 9:
                    textfield = TextField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()
                    if textfield is not None:
                        value = textfield.value
                        if search_keyword is not "" and str(value).lower().find(str(search_keyword).lower()) > -1:
                            search_match.append(value)
                if field.type == 1:
                    integerfield = IntegerField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()
                    if integerfield is not None:
                        value = integerfield.value
                        if search_keyword is not "" and str(value).lower().find(str(search_keyword).lower()) > -1:
                            search_match.append(value)
                if field.type == 2:
                    datetimefield = DateTimeField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()
                    if datetimefield is not None:
                        value = datetimefield.value
                        if search_keyword is not "" and str(value).lower().find(str(search_keyword).lower()) > -1:
                            search_match.append(value)
            if len(search_match) == len(search_keywords):
                search_results.append(instance.id)
            results = Instance.objects.filter(id__in=search_results).order_by('-created_on')
        return results

    def get_success_url(self):
        return reverse('datatype:index', kwargs={'community_id': self.kwargs.get('community_id')})
