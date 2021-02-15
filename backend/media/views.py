from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

# Create your views here.
class EchoViewSet(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        return Response({
            "Result": "Pong"
        })