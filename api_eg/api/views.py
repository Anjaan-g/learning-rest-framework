from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import College, Job, Address
from .serializers import CollegeSerializer, JobSerializer, AddressSerializer

class CollegeView(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
