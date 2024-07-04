from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('contact_us.urls')),
    path('service/' , include('service.urls')),
    path('patient/' , include('patient.urls')),
    path('doctors/' , include('doctor.urls')),
    path('appointments/' , include('appointment.urls'))
    
]

if settings.DEBUG:urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#  szvi svfp hewt lcma