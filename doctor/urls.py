from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpecializationViewSet , DesignationViewSet , DocotorViewSet , AvailableViewSet , ReviewViewSet


router = DefaultRouter()  # Make Router
router.register('specialization', SpecializationViewSet) # Make Antena
router.register('designation', DesignationViewSet) # Make Antena
router.register('doctor', DocotorViewSet) # Make Antena
router.register('avialabletime', AvailableViewSet) # Make Antena
router.register('review', ReviewViewSet) # Make Antena





urlpatterns = [
    path('', include(router.urls)),
]