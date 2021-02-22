from rest_framework import routers, serializers, viewsets
from rest_framework.renderers import JSONRenderer

from media.models import Show

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ['name']

# Create your views here.
class ShowViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer