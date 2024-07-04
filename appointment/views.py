from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerailizers

class AppointmentViewSet(viewsets.ModelViewSet):
  
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerailizers
    
    def get_queryset(self):
        queryset = super().get_queryset() # 7 number line k anlam
        
        patient_id = self.request.query_params.get('patient_id')
        if patient_id :
            queryset = queryset.filter(patient_id = patient_id)
        
        return queryset
        