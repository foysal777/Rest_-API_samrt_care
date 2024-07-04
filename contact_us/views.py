from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import ContactUs
from  . import serializers


class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()    #get all object from models
    serializer_class = serializers.ContactSerailizers  #convert to json code 
