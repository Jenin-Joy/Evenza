from django.shortcuts import render,redirect
from Guest.models import *
from Organization.models import *
from User.models import *

# Create your views here.
def logout(request):
    del request.session["oid"]
    return redirect("Guest:login")

def homepage(request):
    return render(request,'Organization/homepage.html')

def Profile(request):
    org=tbl_Organization.objects.get(id=request.session['oid'])
    return render(request,"Organization/Profile.html",{"org":org})
    
def editprofile(request):
    org=tbl_Organization.objects.get(id=request.session['oid'])
    if request.method=='POST':
        org.org_Name=request.POST.get('name')
        org.org_Email=request.POST.get('mail')
        org.org_Contact=request.POST.get('num')
        org.org_Address=request.POST.get('add')
        org.save()
        return redirect('Organization:editprofile')
    else:
        return render(request,'Organization/Editprofile.html',{'editis':org})

def changepassword(request):
    org=tbl_Organization.objects.get(id=request.session['oid'])
    if request.method=='POST':
        if org.org_Password==request.POST.get("old"):
            if request.POST.get("new")==request.POST.get("confirm"):
                org.org_Password=request.POST.get("confirm")
                org.save()
                return redirect('Organization:changepassword')
            else:
                return render(request,'Organization/Changepassword.html',{'msg':'Error'})
        else:
           return render(request,'Organization/Changepassword.html',{'msg':'Invalid'})
    else:
        return render(request,'Organization/Changepassword.html')
    
def Addevent(request):
    event=tbl_Addevent.objects.all()
    if request.method=="POST":
        tbl_Addevent.objects.create(event_name=request.POST.get('name'),event_poster=request.FILES.get('post'),
                                    event_description=request.POST.get('des'),event_count=request.POST.get('count'),
                                    event_startdate=request.POST.get('sd'),event_enddate=request.POST.get('ed'),
                                    event_amount=request.POST.get('amount'),
                                    org_id=tbl_Organization.objects.get(id=request.session['oid']))
        return redirect('Organization:Addevent')
    else:
        return render(request,'Organization/AddEvent.html',{'Addevent':event})
    
def deleteevent(request,eid):
    tbl_Addevent.objects.get(id=eid).delete()
    return redirect('Organization:Addevent')

def viewbooking(request):
    booking=tbl_Eventbooking.objects.filter(Event_id__org_id=request.session['oid'])
    return render(request,"Organization/Viewbooking.html",{"booking":booking})
    
