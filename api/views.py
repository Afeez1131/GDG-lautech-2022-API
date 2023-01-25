from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions, authentication
from .models import Attendees
from .serializers import AttendeesSerializer, AttendeesDetailSerializer


class AttendeesViewset(viewsets.ModelViewSet):
    serializer_class = AttendeesSerializer
    queryset = Attendees.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]

    # def list(self, request, *args, **kwargs):
    #     context = {'request': request}
    #     serializer = self.serializer_class(self.get_queryset(), many=True, context=context)
    #     return Response(serializer.data)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = AttendeesDetailSerializer(instance)
    #     return Response(serializer.data)
