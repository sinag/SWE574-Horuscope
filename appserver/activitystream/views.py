import json

from django.views import generic

from activitystream.models import ActivityStream
from follow.models import Follow
from root.settings import SERVER_ADDRESS


class IndexView(generic.ListView):
    template_name = 'activitystream/index.html'
    context_object_name = 'activitystreams'

    def get_queryset(self):
        """
        Get activity stream list sorted by creation date
        """
        if self.request.user.is_authenticated:
            activitystreams = ActivityStream.objects.all().order_by('created').reverse()
            follows = Follow.objects.filter(source=self.request.user).all()
            from subscription.models import Subscription
            subscriptions = Subscription.objects.filter(user=self.request.user).all()
            subscribed_communities = []
            to_be_filtered = []
            follow_targets = []
            for subscription in subscriptions:
                subscribed_communities.append(str(subscription.community.id))
            for follow in follows:
                follow_targets.append(str(follow.target.id))
            for activitystream in activitystreams:
                json_data = json.loads(activitystream.data)
                if "actor" in json_data:
                    json_actor = json_data['actor']
                    if "http://" + SERVER_ADDRESS + "/users/view/" in json_actor:
                        json_actor = json_actor.replace("http://" + SERVER_ADDRESS + "/users/view/", "")
                        if str(json_actor) in follow_targets:
                            to_be_filtered.append(activitystream.id)
                if "target" in json_data:
                    json_target = json_data['target']
                    if "http://" + SERVER_ADDRESS + "/users/view/" in json_target:
                        json_target = json_target.replace("http://" + SERVER_ADDRESS + "/users/view/", "")
                        if str(json_target) == str(self.request.user.id):
                            to_be_filtered.append(activitystream.id)
                    if "http://" + SERVER_ADDRESS + "/communities/" in json_target:
                        json_target = json_target.replace("http://" + SERVER_ADDRESS + "/communities/", "")
                        if json_target in subscribed_communities:
                            to_be_filtered.append(activitystream.id)
            activitystreams = activitystreams.filter(id__in=to_be_filtered)
            return activitystreams
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
