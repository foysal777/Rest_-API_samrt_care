from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # Make Router
router.register('Contact_us', views.ContactUsViewSet) # Make Antena

urlpatterns = [
    path('', include(router.urls)),
]