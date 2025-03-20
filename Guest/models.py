from django.db import models
from Admin.models import *
# Create your models here.
class tbl_Serviceprovider(models.Model):
    sp_Name=models.CharField(max_length=30)
    sp_Gmail=models.CharField(max_length=30)
    sp_Contact=models.CharField(max_length=30)
    sp_Address=models.CharField(max_length=30)
    sp_Place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    sp_Password=models.CharField(max_length=30)
    sp_Photo=models.FileField(upload_to="Assets/Servicer/photo/")
    sp_Proof=models.FileField(upload_to="Assets/Servicer/proof/")
    sp_Status=models.IntegerField(default=0)
class tbl_User(models.Model):
    user_Name=models.CharField(max_length=30)
    user_Email=models.CharField(max_length=30)
    user_Contact=models.CharField(max_length=30)
    user_Address=models.CharField(max_length=30)
    user_Password=models.CharField(max_length=30)
class tbl_Organization(models.Model):
    org_Name=models.CharField(max_length=30)
    org_Email=models.CharField(max_length=30)
    org_Contact=models.CharField(max_length=30)
    org_Address=models.CharField(max_length=30)
    org_Place=models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    org_Logo=models.FileField(upload_to="Assets/Organization/logo/")
    org_Proof=models.FileField(upload_to="Assets/Organization/proof/")
    org_Password=models.CharField(max_length=30)
    org_Status=models.IntegerField(default=0)





