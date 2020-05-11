from annotations.models import Annotation
from annotations.serializers import AnnotationSerializer
from rest_framework import viewsets
import json


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned annotations to a given target,
        by filtering against a `target` query parameter in the URL.
        """
        queryset = Annotation.objects.all()
        target = self.request.query_params.get('target', None)
        if target is not None:
            to_be_filtered = []
            for item in queryset:
                json_data = json.loads(item.data)
                if 'target' in json_data:
                    json_target = json_data['target']
                    if 'id' in json_target:
                        if json_target['id'] == target:
                            to_be_filtered.append(item.id)
                    if json_target == target:
                        to_be_filtered.append(item.id)
            queryset = queryset.filter(id__in=to_be_filtered)
        return queryset
