from django.shortcuts import render
from rest_framework import viewsets
from .models import College, Job
from .serializers import CollegeSerializer, JobSerializer

class CollegeView(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer

class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
