from django.db import models
from Guest.models import *

# Create your models here.
class tbl_Addevent(models.Model):
    event_name=models.CharField(max_length=30)
    event_poster=models.FileField(upload_to="Assets/Servicer/photo/")
    event_description=models.CharField(max_length=30)
    event_count=models.CharField(max_length=30)
    event_status=models.IntegerField(default=0)
    event_startdate=models.CharField(max_length=30)
    event_enddate=models.CharField(max_length=30)
    event_amount=models.CharField(max_length=30)
    org_id=models.ForeignKey(tbl_Organization, on_delete=models.CASCADE)
    