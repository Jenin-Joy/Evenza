from django.db import models
from Organization.models import *
from Admin.models import *
from Guest.models import *
from Serviceprovider.models import *
from User.models import *

#Create your models here.
class tbl_Booking(models.Model):
    Booking_date=models.DateField(auto_now_add=True)
    Booking_todate=models.DateField(null=True)
    Place_id=models.ForeignKey(tbl_place, on_delete=models.CASCADE, null=True)
    Booking_description=models.CharField(max_length=30)
    Booking_amount=models.CharField(max_length=30)
    Booking_status=models.IntegerField(default=0)
    User_id=models.ForeignKey(tbl_User, on_delete=models.CASCADE)
    Packagetype_id=models.ForeignKey(tbl_Packagetype, on_delete=models.CASCADE, null=True)
 
class tbl_Eventbooking(models.Model):
    Eventbooking_count=models.CharField(max_length=30)
    Event_id=models.ForeignKey(tbl_Addevent, on_delete=models.CASCADE)
    User_id=models.ForeignKey(tbl_User, on_delete=models.CASCADE)
    Eventbooking_amount=models.CharField(max_length=30)
    Eventbooking_status=models.IntegerField(default=0)

class tbl_Cart(models.Model):
    Package=models.ForeignKey(tbl_Addpackage, on_delete=models.CASCADE)
    Booking=models.ForeignKey(tbl_Booking, on_delete=models.CASCADE)
    Cart_status=models.IntegerField(default=0)

class tbl_Custombooking(models.Model):
    Custombooking_date=models.DateField(auto_now_add=True)
    Custombooking_todate=models.DateField(null=True)
    Place=models.ForeignKey(tbl_place, on_delete=models.CASCADE, null=True)
    Custombooking_description=models.CharField(max_length=30)
    Custombooking_amount=models.CharField(max_length=30)
    User=models.ForeignKey(tbl_User, on_delete=models.CASCADE)
    Serviceprovider=models.ForeignKey(tbl_Serviceprovider, on_delete=models.CASCADE)
    Packagetype=models.ForeignKey(tbl_Packagetype, on_delete=models.CASCADE, null=True)
    Custombooking_status=models.IntegerField(default=0)

class tbl_Complaint(models.Model):
    Complaint_title=models.CharField(max_length=30)
    Complaint_content=models.CharField(max_length=30)
    Complaint_date=models.DateField(auto_now_add=True)
    Complaint_status=models.IntegerField(default=0)
    Complaint_reply=models.CharField(max_length=30)
    User=models.ForeignKey(tbl_User, on_delete=models.CASCADE)
    package=models.ForeignKey(tbl_Addpackage, on_delete=models.CASCADE,null=True)
    Custombooking=models.ForeignKey(tbl_Custombooking, on_delete=models.CASCADE,null=True)

class tbl_Feedback(models.Model):
    Feedback_content=models.CharField(max_length=30)
    user = models.ForeignKey(tbl_User, on_delete=models.CASCADE)
    
class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_User,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    servicerprovider=models.ForeignKey(tbl_Serviceprovider,on_delete=models.CASCADE,null=True)
    organization=models.ForeignKey(tbl_Organization,on_delete=models.CASCADE,null=True)
    datetime=models.DateTimeField(auto_now_add=True)