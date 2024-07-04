from rest_framework import viewsets
from .models import Service
from . import serializers

class ServiceViewSet(viewsets.ModelViewSet):
  
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerailizers