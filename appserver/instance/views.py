from django.db import transaction
from django.urls import reverse
from django.views.generic import FormView
from datatype.models import DataType
from datetimefield.models import DateTimeField
from instance.forms import DynamicPost
from integerfield.models import IntegerField
from textfield.models import TextField
from .models import Instance

"""
Class based view to create new instance
"""


class CreateView(FormView):
    template_name = 'instance/create.html'
    form_class = DynamicPost

    def form_valid(self, form):
        """
        Assign instance data inside a transaction object
        """
        with transaction.atomic():
            instance = Instance(datatype=DataType.objects.get(id=self.kwargs.get('datatype_id')),
                                author=self.request.user)
            instance.save()
            for field in DataType.objects.get(id=self.kwargs.get('datatype_id')).fields():
                if field.type == 0 or field.type == 4 or field.type == 5 or field.type == 6 or field.type == 7 or field.type == 8 or field.type == 9:
                    if field.name == 'Semantic Tags':
                        value = TextField(value=form.data['hdn_tags'], property_id=field.id, instance_id=instance.id)
                        value.save()
                    else:
                        value = TextField(value=form.data[field.name], property_id=field.id, instance_id=instance.id)
                        value.save()
                if field.type == 1:
                    if form.data[field.name] is not '':
                        value = IntegerField(value=int(form.data[field.name]), property_id=field.id,
                                             instance_id=instance.id)
                    else:
                        value = IntegerField(value=None, property_id=field.id,
                                             instance_id=instance.id)
                    value.save()
                if field.type == 2:
                    if form.data[field.name] is not '':
                        value = DateTimeField(value=form.data[field.name], property_id=field.id,
                                              instance_id=instance.id)
                    else:
                        value = DateTimeField(value=None, property_id=field.id,
                                              instance_id=instance.id)
                    value.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:posts',
                       kwargs={'pk': DataType.objects.get(id=self.kwargs.get('datatype_id')).community.id})


"""
Class based view to delete existing instance
"""


class DeleteView(FormView):
    template_name = 'instance/delete.html'
    form_class = DynamicPost

    def form_valid(self, form):
        """
        Delete instance data inside a transaction object
        """
        with transaction.atomic():
            instance = Instance.objects.get(id=self.kwargs.get('pk'))
            for field in DataType.objects.get(id=instance.datatype_id).fields():
                if field.type == 0 or field.type == 4 or field.type == 5 or field.type == 6 or field.type == 7 or field.type == 8 or field.type == 9:
                    value = TextField.objects.filter(instance_id=instance.id).filter(property_id=field.id)
                    value.delete()
                if field.type == 1:
                    value = IntegerField.objects.filter(instance_id=instance.id).filter(property_id=field.id)
                    value.delete()
                if field.type == 2:
                    value = DateTimeField.objects.filter(instance_id=instance.id).filter(property_id=field.id)
                    value.delete()
            instance.delete()
            return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:posts',
                       kwargs={'pk': DataType.objects.get(id=self.kwargs.get('datatype_id')).community.id})


"""
Class based view to update existing instance
"""


class UpdateView(FormView):
    template_name = 'instance/update.html'
    form_class = DynamicPost

    def form_valid(self, form):
        """
        Update instance data inside a transaction object
        """
        with transaction.atomic():
            instance = Instance.objects.get(id=self.kwargs.get('pk'))

            for field in DataType.objects.get(id=instance.datatype.id).fields():
                if field.type == 0 or field.type == 4 or field.type == 5 or field.type == 6 or field.type == 7 or field.type == 8 or field.type == 9:
                    textfield = TextField.objects.filter(instance_id=instance.id).filter(property_id=field.id).first()
                    if field.name == 'Semantic Tags':
                        new_value = form.data['hdn_tags']
                    else:
                        new_value = form.data[field.name]
                    if textfield is None:
                        textfield = TextField(value=new_value, property_id=field.id,
                                              instance_id=instance.id)
                    else:
                        textfield.value = new_value
                    textfield.save()
                if field.type == 1:
                    integerfield = IntegerField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()
                    if integerfield is None:
                        integerfield = IntegerField(value=form.data[field.name], property_id=field.id,
                                                    instance_id=instance.id)
                    else:
                        if form.data[field.name] == '':
                            integerfield.value = None
                        else:
                            integerfield.value = form.data[field.name]
                    integerfield.save()
                if field.type == 2:
                    datetimefield = DateTimeField.objects.filter(instance_id=instance.id).filter(
                        property_id=field.id).first()
                    if datetimefield is None:
                        datetimefield = DateTimeField(value=form.data[field.name], property_id=field.id,
                                                      instance_id=instance.id)
                    else:
                        if form.data[field.name] == '':
                            datetimefield.value = None
                        else:
                            datetimefield.value = form.data[field.name]
                    datetimefield.save()

            return super().form_valid(form)

    def get_success_url(self):
        return reverse('community:posts',
                       kwargs={
                           'pk': Instance.objects.get(id=self.kwargs.get('pk')).datatype.community.id})
