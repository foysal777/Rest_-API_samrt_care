
   # ********************************* Api Secure Mode ************************************

from django.shortcuts import render
from rest_framework import viewsets
 # read only for unAuthenticated users code ************************************
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters, pagination
# Create your views here.
from .models import Specialization, Designation , Doctor , AvailableTime ,Review
from  .serializers import  SpecializationSerailizers , DesignationSerailizers , DoctorSerailizers , AvailableTimeSerailizers , ReviewSerailizers


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()    #get all object from models
    serializer_class = SpecializationSerailizers  #convert to json code 



class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()    
    serializer_class = DesignationSerailizers  



# Doctor pagination part *****************************
class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100 

class DocotorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()    
    serializer_class = DoctorSerailizers  
    
# Doctor pagination part *****************************

    pagination_class = DoctorPagination


    
class AvailableViewSet(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()    
  
    serializer_class = AvailableTimeSerailizers  
    
    
    
class ReviewViewSet(viewsets.ModelViewSet):
    # read only for unAuthenticated users code ************************************
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()    
    serializer_class = ReviewSerailizers