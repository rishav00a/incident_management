from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from incident.serializers import IncidentSerializer
from incident.models import Incident
from rest_framework.viewsets import ModelViewSet
# Create your views here.



class IncidentViewSet(ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
