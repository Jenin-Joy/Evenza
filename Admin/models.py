from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)
class tbl_AdminRegistration(models.Model):
    Admin_name=models.CharField(max_length=30)
    Mail=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
class tbl_Eventtype(models.Model):
    Eventtype=models.CharField(max_length=30)
class tbl_place(models.Model):
    Place=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_Packagetype(models.Model):
    Package_type=models.CharField(max_length=30)