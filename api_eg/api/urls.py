from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('colleges', views.CollegeView)
router.register('jobs', views.JobView)
router.register('addresses', views.AddressView)

urlpatterns = [
    path('', include(router.urls)),
    
]
