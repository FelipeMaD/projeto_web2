from rest_framework import viewsets, permissions
from appteste import models
from appteste.api import serializers
from .permissions import IsInSpecificGroup
import logging

logger = logging.getLogger('custom')

class PixelsViewSet(viewsets.ModelViewSet):
    queryset = models.Pixels.objects.all()
    serializer_class = serializers.Pixels
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup, permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        logger.info(f'Novo pixel criado no banco de pixels')
        serializer.save()

