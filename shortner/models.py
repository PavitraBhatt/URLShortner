from django.db import models
import uuid

class Url(models.Model):
    link = models.URLField()
    uuid = models.CharField(max_length=36, unique=True, default=str(uuid.uuid4()))
    expiry_date = models.DateTimeField(null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)
