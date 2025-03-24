from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def logout(request):
    del request.session["aid"]
    return redirect("Guest:login")

def District(request):
    dist=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get('district'))
        return redirect('Admin:District')
    else:
        return render(request,'Admin/District.html',{'district':dist})
def AdminRegistration(request):
    admin=tbl_AdminRegistration.objects.all()
    if request.method=="POST":
        tbl_AdminRegistration.objects.create(Admin_name=request.POST.get('admin'),Mail=request.POST.get('mail'),Password=request.POST.get('pass'))
        return redirect('Admin:AdminRegistration')
    else:
        return render(request,'Admin/AdminRegistration.html',{'adminreg':admin})
def Eventtype(request):
    event=tbl_Eventtype.objects.all()
    if request.method=="POST":
        tbl_Eventtype.objects.create(Eventtype=request.POST.get('ename'))
        return redirect('Admin:Eventtype')
    else:
        return render(request,'Admin/Eventtype.html',{'eventype':event})
def place(request):
    pl=tbl_place.objects.all()
    di=tbl_district.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(Place=request.POST.get('place'),district=district)
        return redirect('Admin:place')
    else:
        return render(request,'Admin/place.html',{'district':di,'place':pl})
def deleteplace(request,pid):
    tbl_place.objects.get(id=pid).delete()
    return redirect('Admin:place')
def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:District')
def deleteadmin(request,aid):
    tbl_AdminRegistration.objects.get(id=aid).delete()
    return redirect('Admin:AdminRegistration')
def deleteevent(request,eid):
    tbl_Eventtype.objects.get(id=eid).delete()
    return redirect('Admin:Eventtype')
def editdistrict(request,did):
    dis=tbl_district.objects.get(id=did)
    if request.method=='POST':
        dis.district_name=request.POST.get('district')
        dis.save()
        return redirect('Admin:District')
    else:
        return render(request,'Admin/District.html',{'editdis':dis})
def editadmin(request,aid):
    admin=tbl_AdminRegistration.objects.get(id=aid)
    if request.method=='POST':
        admin.Admin_name=request.POST.get('admin')
        admin.Mail=request.POST.get('mail')
        admin.save()
        return redirect('Admin:AdminRegistration')
    else:
        return render(request,'Admin/AdminRegistration.html',{'editadmin':admin})
def editevent(request,eid):
    event=tbl_Eventtype.objects.get(id=eid)
    if request.method=='POST':
        event.Eventtype=request.POST.get('ename')
        event.save()
        return redirect('Admin:Eventtype')
    else:
        return render(request,'Admin/Eventtype.html',{'editevent':event})
def editplace(request,pid):
    di=tbl_district.objects.all()
    pla=tbl_place.objects.get(id=pid)
    if request.method=='POST':
        district=tbl_district.objects.get(id=request.POST.get('sel_district'))
        pla.district=district
        pla.Place=request.POST.get('place')
        pla.save()
        return redirect('Admin:place')
    else:
        return render(request,'Admin/place.html',{'editpla':pla,'district':di})
    
def homepage(request):
    return render(request,'Admin/homepage.html')

def Packagetype(request):
    pack=tbl_Packagetype.objects.all()
    if request.method=="POST":
        tbl_Packagetype.objects.create(Package_type=request.POST.get('pname'))
        return redirect('Admin:Packagetype')
    else:
        return render(request,'Admin/Packagetype.html',{'packagetype':pack})
    
def editpackage(request,pid):
    pack=tbl_Packagetype.objects.get(id=pid)
    if request.method=='POST':
        pack.Package_type=request.POST.get('pname')
        pack.save()
        return redirect('Admin:Packagetype')
    else:
        return render(request,'Admin/Packagetype.html',{'editpackage':pack})
    
def deletepackage(request,pid):
    tbl_Packagetype.objects.get(id=pid).delete()
    return redirect('Admin:Packagetype')

def viewcomplaint(request):
    complaint=tbl_Complaint.objects.filter(package__isnull=True, Custombooking__isnull=True, Complaint_status=0)
    return render(request,"Admin/ViewComplaint.html",{"complaint":complaint})

def reply(request,id):
    complaint=tbl_Complaint.objects.get(id=id)
    if request.method=='POST':
        complaint.Complaint_reply=request.POST.get('reply')
        complaint.Complaint_status = 1
        complaint.save()
        return redirect('Admin:viewcomplaint')
    else:
        return render(request,'Admin/Reply.html',{'reply':complaint})
    
def replyedcomplaint(request):
    replyed=tbl_Complaint.objects.filter(package__isnull=True, Custombooking__isnull=True, Complaint_status=1)
    return render(request,"Admin/ReplyedComplaint.html",{"replyed":replyed})

def viewfeedback(request):
    feed = tbl_Feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{"data":feed})

def neworganization(request):
    org = tbl_Organization.objects.filter(org_Status=0)
    return render(request,"Admin/NewOrganization.html",{"data":org})

def newserviceprovider(request):
    ser = tbl_Serviceprovider.objects.filter(sp_Status=0)
    return render(request,"Admin/NewServiceprovider.html",{"data":ser})

def acceptedorganization(request):
    org = tbl_Organization.objects.filter(org_Status=1)
    return render(request,"Admin/AcceptedOrganization.html",{"data":org})

def acceptedserviceprovider(request):
    ser = tbl_Serviceprovider.objects.filter(sp_Status=1)
    return render(request,"Admin/AcceptedList.html",{"data":ser})

def rejectedorganization(request):
    org = tbl_Organization.objects.filter(org_Status=2)
    return render(request,"Admin/RejectedOrganization.html",{"data":org})

def rejectedserviceprovider(request):
    ser = tbl_Serviceprovider.objects.filter(sp_Status=2)
    return render(request,"Admin/RejectList.html",{"data":ser})

def verifyorganization(request, id, status):
    org = tbl_Organization.objects.get(id=id)
    org.org_Status = status
    org.save()
    user = org.org_Name
    user_email = org.org_Email
    if status == 1:
        send_mail(
            f"Your Event Registration is Confirmed, {user}!",
            (f"Dear {user},\r\n"
            "Thank you for registering for an event with Evenza! We are excited to confirm your registration and can't wait for you to join us. "
            "Your participation is important to us, and we are here to ensure everything runs smoothly.\r\n"
            "if you have any questions or need assistance, feel free to reach out.\r\n"
            "Warm regards,\r\n"
            "The Evenza Team"),
            settings.EMAIL_HOST_USER,
            [user_email],
        )

    else:
        send_mail(
            f"Your Event Registration Status - Evenza",
            (f"Dear {user},\r\n"
            "Thank you for your interest in registering for an event with Evenza. Unfortunately, we regret to inform you that your registration could not be processed at this time.\r\n"
            "This could be due to various reasons such as some verification issue. We understand this may be disappointing, but please know we value your interest and would love to have you join us in the future.\r\n"
            "If you have any questions or need further clarification, please donot hesitate to reach out.\r\n"
            "Thank you again for considering Evenza. We hope to welcome you soon.\r\n"
            "Warm regards,\r\n"
            "The Evenza Team"),
            settings.EMAIL_HOST_USER,
            [user_email],
        )

    return redirect("Admin:homepage")

def verifyserviceprovider(request, id, status):
    ser = tbl_Serviceprovider.objects.get(id=id)
    ser.sp_Status = status
    ser.save()
    user = ser.sp_Name
    user_email = ser.sp_Gmail
    if status == 1:
        send_mail(
            f"Your Event Registration is Confirmed, {user}!",
            (f"Dear {user},\r\n"
            "Thank you for registering for an event with Evenza! We are excited to confirm your registration and can't wait for you to join us. "
            "Your participation is important to us, and we are here to ensure everything runs smoothly.\r\n"
            "if you have any questions or need assistance, feel free to reach out.\r\n"
            "Warm regards,\r\n"
            "The Evenza Team"),
            settings.EMAIL_HOST_USER,
            [user_email],
        )

    else:
        send_mail(
            f"Your Event Registration Status - Evenza",
            (f"Dear {user},\r\n"
            "Thank you for your interest in registering for an event with Evenza. Unfortunately, we regret to inform you that your registration could not be processed at this time.\r\n"
            "This could be due to various reasons such as some verification issue. We understand this may be disappointing, but please know we value your interest and would love to have you join us in the future.\r\n"
            "If you have any questions or need further clarification, please donot hesitate to reach out.\r\n"
            "Thank you again for considering Evenza. We hope to welcome you soon.\r\n"
            "Warm regards,\r\n"
            "The Evenza Team"),
            settings.EMAIL_HOST_USER,
            [user_email],
        )
    return redirect("Admin:homepage")