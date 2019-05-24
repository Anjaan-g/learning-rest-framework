from rest_framework import serializers
from .models import College, Job

class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ['id','url', 'name', 'address',]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'url', 'position', 'salary']
