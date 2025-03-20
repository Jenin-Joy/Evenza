from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Serviceprovider.models import *
from User.models import *
from django.http import JsonResponse

# Create your views here.
def logout(request):
    del request.session["spid"]
    return redirect("Guest:login")

def Addpackage(request):
    pack=tbl_Addpackage.objects.all()
    packagetype=tbl_Packagetype.objects.all()
    if request.method=="POST":
        tbl_Addpackage.objects.create(pack_name=request.POST.get('name'),pack_description=request.POST.get('des'),
                                      pack_typeid=tbl_Packagetype.objects.get(id=request.POST.get('sel_type')),
                                      pack_spid=tbl_Serviceprovider.objects.get(id=request.session['spid']),
                                      pack_amount=request.POST.get('num'),pack_photo=request.FILES.get('photo'))
        return redirect('Serviceprovider:Addpackage')
    else:
        return render(request,'Serviceprovider/Addpackage.html',{'addpackage':pack,"packagetype":packagetype})
    
def deletepackage(request,pid):
    tbl_Addpackage.objects.get(id=pid).delete()
    return redirect('Serviceprovider:Addpackage')

def homepage(request):
    return render(request,'Serviceprovider/homepage.html')

def Profile(request):
    ser=tbl_Serviceprovider.objects.get(id=request.session['spid'])
    return render(request,"Serviceprovider/Profile.html",{"sp":ser})
    
def editprofile(request):
    ser=tbl_Serviceprovider.objects.get(id=request.session['spid'])
    if request.method=='POST':
        ser.sp_Name=request.POST.get('name')
        ser.sp_Gmail=request.POST.get('mail')
        ser.sp_Contact=request.POST.get('num')
        ser.sp_Address=request.POST.get('add')
        ser.save()
        return redirect('Serviceprovider:editprofile')
    else:
        return render(request,'Serviceprovider/Editprofile.html',{'editis':ser})

def changepassword(request):
    ser=tbl_Serviceprovider.objects.get(id=request.session['spid'])
    if request.method=='POST':
        if ser.sp_Password==request.POST.get("old"):
            if request.POST.get("new")==request.POST.get("confirm"):
                ser.sp_Password=request.POST.get("confirm")
                ser.save()
                return redirect('Serviceprovider:changepassword')
            else:
                return render(request,'Serviceprovider/Changepassword.html',{'msg':'Error'})
        else:
           return render(request,'Serviceprovider/Changepassword.html',{'msg':'Invalid'})
    else:
        return render(request,'Serviceprovider/Changepassword.html')

def addwork(request):
    work = tbl_work.objects.filter(serviceprovider=request.session["spid"])
    if request.method == "POST":
        tbl_work.objects.create(work_name=request.POST.get("txt_name"),work_description=request.POST.get("txt_description"),
                                work_photo=request.FILES.get("txt_photo"),
                                serviceprovider=tbl_Serviceprovider.objects.get(id=request.session["spid"]))
        return redirect("Serviceprovider:addwork")
    else:
        return render(request,"Serviceprovider/Addwork.html",{"work":work})
    
def deletework(request, id):
    tbl_work.objects.get(id=id).delete()
    return redirect("Serviceprovider:addwork")

def gallery(request, id):
    gallery = tbl_gallery.objects.filter(work=id)
    if request.method == "POST":
        tbl_gallery.objects.create(gallery_photo=request.FILES.get("txt_photo"),work=tbl_work.objects.get(id=id))
        return redirect("Serviceprovider:gallery", id)
    else:
        return render(request,"Serviceprovider/Addphoto.html",{"gallery":gallery,"id":id})
    
def deletegallery(request, id, workid):
    tbl_gallery.objects.get(id=id).delete()
    return redirect("Serviceprovider:gallery", workid)

def viewpackagebooking(request):
    booking=tbl_Booking.objects.filter(tbl_cart__Package__pack_spid=request.session['spid'])
    return render(request,"Serviceprovider/ViewBookingpackage.html",{"booking":booking})

def bookingstatus(request,bid,value):
    booking=tbl_Booking.objects.get(id=bid)
    booking.Booking_status=value
    booking.save()
    return redirect("Serviceprovider:viewpackagebooking")

def viewcustombooking(request):
    custom=tbl_Custombooking.objects.filter(Serviceprovider=request.session["spid"])
    return render(request,"Serviceprovider/ViewBookingcustom.html",{"custom":custom})

def updatecustom(request, id, status):
    cus = tbl_Custombooking.objects.get(id=id)
    cus.Custombooking_status = status
    cus.save()
    msg = ""
    if status == 1:
        msg = "Custome Request Accepted"
    else:
        msg = "Custome Request Rejected"
    return render(request,"Serviceprovider/ViewBookingcustom.html",{"msg":msg})

def ajaxaddamount(request):
    cus = tbl_Custombooking.objects.get(id=request.GET.get("cid"))
    cus.Custombooking_amount = request.GET.get("amount")
    cus.Custombooking_status=3
    cus.save()
    return JsonResponse({"msg":"Amount Updated"})

def viewcomplaint(request):
    complaint=tbl_Complaint.objects.filter(package__pack_spid=request.session['spid'],Complaint_status=0)
    custom = tbl_Complaint.objects.filter(Custombooking__Serviceprovider=request.session["spid"],Complaint_status=0)
    return render(request,"Serviceprovider/ViewComplaint.html",{"complaint":complaint,"custom":custom})

def reply(request, id):
    complaint=tbl_Complaint.objects.get(id=id)
    if request.method=='POST':
        complaint.Complaint_reply=request.POST.get('reply')
        complaint.Complaint_status = 1
        complaint.save()
        return redirect('Serviceprovider:viewcomplaint')
    else:
        return render(request,'Serviceprovider/Reply.html')
    
def replyedcomplaint(request):
    replyed=tbl_Complaint.objects.filter(package__pack_spid=request.session['spid'],Complaint_status=1)
    custom = tbl_Complaint.objects.filter(Custombooking__Serviceprovider=request.session["spid"],Complaint_status=1)
    return render(request,"Serviceprovider/ReplyedComplaint.html",{"replyed":replyed,"custom":custom})

def viewfeedback(request):
    fb=tbl_Feedback.objects.filter()
    return render(request,"Serviceprovider/ViewFeedback.html",{"view":fb})