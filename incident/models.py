from django.db import models
from handler.models import Handler
import uuid
from incident.utils import *
# Create your models here.
class Incident(models.Model):
    STATUS_CHOICES = (
        ('pending', "Pending"),
        ('assigned', "assigned"),
        ("resolved","Resolved")
    )
    incident_id  = models.UUIDField(primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    type = models.CharField(max_length=255)
    severity = models.IntegerField()
    timestamp = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=255, default="pending")
    assigned_to = models.ForeignKey(Handler, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return str(self.incident_id)
    
    def save(self, *args, **kwargs):
        process_type = "new"
        pre_save_data =  None
        print(self, args, kwargs)
        if self.__class__.objects.filter(incident_id=self.incident_id).exists():
            process_type = "updated"
            pre_save_data = self.__class__.objects.get(incident_id=self.incident_id)
        super(Incident, self).save(*args, **kwargs)

        process_incidents(process_type, pre_save_data, self)
