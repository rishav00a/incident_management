from django.db import models

# Create your models here.
class Handler(models.Model):
    handler_status_choices = (
        ('unavailable', "Unavailable"),
        ('available', "Available"),
    )
    name= models.CharField(max_length=255)
    status = models.CharField(max_length=255, default="available")
    cases_handled_today = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name