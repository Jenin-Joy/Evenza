from django.db import models
from Guest.models import *
from Admin.models import *

# Create your models here.

class tbl_Addpackage(models.Model):
    pack_name=models.CharField(max_length=30)
    pack_description=models.CharField(max_length=30)
    pack_typeid=models.ForeignKey(tbl_Packagetype, on_delete=models.CASCADE)
    pack_spid=models.ForeignKey(tbl_Serviceprovider, on_delete=models.CASCADE)
    pack_amount=models.CharField(max_length=30)
    pack_photo=models.FileField(upload_to="Assets/Servicer/photo/")
    
class tbl_work(models.Model):
    work_name = models.CharField(max_length=30)
    work_description = models.CharField(max_length=100) 
    work_photo = models.FileField(upload_to="Assets/ServiceProvider/Work/") 
    serviceprovider = models.ForeignKey(tbl_Serviceprovider, on_delete=models.CASCADE)

class tbl_gallery(models.Model):
    gallery_photo = models.FileField(upload_to="Assets/ServiceProvider/Gallery/")
    work = models.ForeignKey(tbl_work, on_delete=models.CASCADE)