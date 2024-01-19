from rest_framework.serializers import ModelSerializer
from incident.models import Incident
class IncidentSerializer(ModelSerializer):
    class Meta:
        model = Incident
        fields = ['incident_id', 'type', 'severity', 'timestamp', 'description', 'status', 'assigned_to']
        read_only_fields = ('incident_id',)