from django.views import generic

from activitystream.models import ActivityStream


class IndexView(generic.ListView):
    template_name = 'activitystream/index.html'
    context_object_name = 'activitystreams'

    def get_queryset(self):
        """
        Get activity stream list sorted by creation date
        """
        if self.request.user.is_authenticated:
            queryset = ActivityStream.objects.all()
            return queryset
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
