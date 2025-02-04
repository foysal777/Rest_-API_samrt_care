from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # Make Router
router.register('list', views.PatientViewSet) # Make Antena

urlpatterns = [
    path('', include(router.urls)),
    path('register/' , views.userRegistration.as_view() , name= 'register'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),

]

# registration part 

# {
    
#     "username": "sipuu"
#     "password" : "Shipu55@@"
# }