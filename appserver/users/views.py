from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, View
from django.views import generic
from .models import CustomUser

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ViewProfilePage(generic.ListView):
    model = CustomUser
    template_name = 'user/profilepage.html'
    context_object_name = 'user'

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.kwargs.get('pk')).first()


class UpdateProfilePage(UpdateView):
    model = CustomUser
    fields = ['bio', 'profile_pic', ]
    template_name = 'user/update.html'

    def get_success_url(self):
        user_id = CustomUser.objects.filter(id=self.kwargs.get('pk')).first().id
        return reverse('users:view', args=(user_id,))

    def get_queryset(self):
        """
        Get comment details to update
        """
        return CustomUser.objects.filter(id=self.kwargs.get('pk'))
