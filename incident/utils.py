from handler.models import Handler
from incident.models import *


def assign_handler(incident_obj, handler_obj):
    incident_obj.status = "assigned"
    incident_obj.assigned_to = handler_obj
    incident_obj.save()

    handler_obj.status = "unavailable"
    handler_obj.cases_handled_today = handler_obj.cases_handled_today + 1
    handler_obj.save()

def set_handler_available(incident_obj):
    incident_obj.assigned_to.status = "available"
    incident_obj.assigned_to.save()

# process_type : ["new", "updated"]
def process_incidents(process_type, incident_obj_old, incident_obj_new):
    incedent_model = incident_obj_new.__class__
    if process_type == "updated":
        if incident_obj_old.status == "assigned" and incident_obj_new.status == "resolved":
            set_handler_available(incident_obj_new)

    if incedent_model.objects.filter(status="pending").exists():
        next_priority_incident = incedent_model.objects.filter(status="pending").order_by("severity", "timestamp").first()
    
        if Handler.objects.filter(status="available").exists():
            available_handler = Handler.objects.filter(status="available").order_by("cases_handled_today").first()

            print(available_handler)
            assign_handler(next_priority_incident, available_handler)
    
