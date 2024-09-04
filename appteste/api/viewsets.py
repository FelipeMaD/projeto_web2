from rest_framework import viewsets, permissions
from appteste import models
from appteste.api import serializers
from .permissions import IsInSpecificGroup


class PixelsViewSet(viewsets.ModelViewSet):
    queryset = models.Pixels.objects.all()
    serializer_class = serializers.Pixels
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup, permissions.DjangoModelPermissions]


