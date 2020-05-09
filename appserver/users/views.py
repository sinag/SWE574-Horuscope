from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, View
from django.views import generic
from .models import AbstractUser, CustomUser

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ViewProfilePage(generic.ListView):
    model = CustomUser
    template_name = 'user/profilepage.html'
    context_object_name = 'users'

    ## gets any users page with PK and returns to page as a queryset
    def get_queryset(self):
        print(CustomUser.objects.filter(id=self.kwargs.get('pk')).values('email'))
        return CustomUser.objects.filter(id=self.kwargs.get('pk'))

'''  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['instance'] = Instance.objects.all().filter(id=self.kwargs.get('instance_id')).get()
        return context'''


class UpdateProfilePage(UpdateView):
    model = CustomUser
    fields = ['bio', 'profile_pic']
    template_name = 'user/update.html'

    def get_success_url(self):
        user_id = CustomUser.objects.filter(id=self.kwargs.get('pk')).first().id
        #return reverse('users:userview', args=(user_id,))
        return reverse('users:view', args=(user_id,))

    def get_queryset(self):
        """
        Get comment details to update
        """
        return CustomUser.objects.filter(id=self.kwargs.get('pk'))