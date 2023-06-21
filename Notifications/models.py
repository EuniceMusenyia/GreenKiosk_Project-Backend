from django.db import models

# Create your models here.
class  Notifications(models.Model):
    # recipient = models.ForeignKey()
    message = models.TextField(max_length=100)
    date = models.DateField()
    notification_type = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):           ####self acts as string representation of the class//**
        return self.notification_type