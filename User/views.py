from django.shortcuts import render,redirect
from Guest.models import * 
from Serviceprovider.models import * 
from Organization.models import *
from User.models import * 
from Admin.models import * 
from django.http import JsonResponse 

# Create your views here.
def logout(request):
    del request.session["uid"]
    return redirect("Guest:login")

def homepage(request):
    return render(request,'User/homepage.html')

def Profile(request):
    user=tbl_User.objects.get(id=request.session['uid'])
    return render(request,"User/Profile.html",{"User":user})
    
def editprofile(request):
    user=tbl_User.objects.get(id=request.session['uid'])
    if request.method=='POST':
        user.user_Name=request.POST.get('name')
        user.user_Email=request.POST.get('mail')
        user.user_Contact=request.POST.get('num')
        user.user_Address=request.POST.get('add')
        user.save()
        return redirect('User:editprofile')
    else:
        return render(request,'User/Editprofile.html',{'editis':user})

def changepassword(request):
    user=tbl_User.objects.get(id=request.session['uid'])
    if request.method=='POST':
        if user.user_Password==request.POST.get("old"):
            if request.POST.get("new")==request.POST.get("confirm"):
                user.user_Password=request.POST.get("confirm")
                user.save()
                return redirect('User:changepassword')
            else:
                return render(request,'User/Changepassword.html',{'msg':'Error'})
        else:
           return render(request,'User/Changepassword.html',{'msg':'Invalid'})
    else:
        return render(request,'User/Changepassword.html')
    
def viewsp(request):
    di=tbl_district.objects.all()
    sp=tbl_Serviceprovider.objects.all()
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    for i in sp:
        tot=0
        ratecount=tbl_rating.objects.filter(servicerprovider=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(servicerprovider=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(sp,parry)
    return render(request,"User/ViewServiceprovider.html",{'view':datas,'district':di,"ar":ar})

def viewservicerprofile(request,spid):
    pro=tbl_Serviceprovider.objects.get(id=spid)
    return render(request,"User/ViewServicerprofile.html",{'view':pro})

def viewpackage(request,pid):
    pack=tbl_Addpackage.objects.filter(pack_spid=pid)
    return render(request,"User/Viewpackage.html",{'viewpackage':pack,"id":pid})

def viewwork(request,wid):
    wk=tbl_work.objects.filter(serviceprovider=wid)
    return render(request,"User/Viewwork.html",{'viewwork':wk})

def booknow(request, id):
    di=tbl_district.objects.all()
    packagetype=tbl_Packagetype.objects.all()
    if request.method == "POST":
        book = tbl_Booking.objects.get(id=id)
        book.Booking_todate = request.POST.get("txt_date")
        book.Booking_description = request.POST.get("txt_description")
        book.Place_id = tbl_place.objects.get(id=request.POST.get("select_place"))
        book.Packagetype_id = tbl_Packagetype.objects.get(id=request.POST.get("sel_type"))
        book.Booking_status = 2
        book.save()
        return render(request,'User/Booknow.html',{'msg':"Your Package is Booked And waiting for verification"})
    else:
        return render(request,'User/Booknow.html',{'district':di,"packaget":packagetype})
    
def viewgallery(request):
    vg=tbl_gallery.objects.all()
    return render(request,"User/Viewgallery.html",{'viewgallery':vg})
    
def viewevent(request):
    eve=tbl_Addevent.objects.all()
    return render(request,"User/Viewevents.html",{'viewevent':eve})    
    
def bookcount(request,id):
    event = tbl_Addevent.objects.get(id=id)
    amount = event.event_amount
    if request.method=="POST":
        Event = tbl_Eventbooking.objects.create(Eventbooking_count=request.POST.get('count'),
                                        Event_id=tbl_Addevent.objects.get(id=id),
                                        User_id=tbl_User.objects.get(id=request.session['uid']),
                                        Eventbooking_amount=request.POST.get('txtamount'))
        return redirect('User:ticketpayment',Event.id)
    else:
        return render(request,'User/Bookcount.html',{"amount":amount})
    
def ticketpayment(request,id):
   booking = tbl_Eventbooking.objects.get(id=id)
   amount = booking.Eventbooking_amount
   if request.method == "POST":
      booking.Eventbooking_status = 1
      booking.save()
      return redirect("User:loader")
   else:
      return render(request,"User/Payment.html", {"total":amount})

def Addcart(request,pid,id):
    packagedata=tbl_Addpackage.objects.get(id=pid)
    userdata=tbl_User.objects.get(id=request.session["uid"])
    bookingcount=tbl_Booking.objects.filter(User_id=userdata,Booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_Booking.objects.get(User_id=userdata,Booking_status=0)
        cartcount=tbl_Cart.objects.filter(Booking=bookingdata,Package=packagedata).count()
        if cartcount>0:
            return render(request,"User/Viewpackage.html",{'msg':"Already Booked", "id":id})
        else:
            tbl_Cart.objects.create(Booking=bookingdata,Package=packagedata)
            return render(request,"User/Viewpackage.html",{'msg':"Package Booked", "id":id})
    else:
        bookingdata = tbl_Booking.objects.create(User_id=userdata)
        tbl_Cart.objects.create(Booking=tbl_Booking.objects.get(id=bookingdata.id),Package=packagedata)
        return render(request,"User/Viewpackage.html",{'msg':"Package Booked", "id":id})

def mypackbooking(request):
    if request.method=="POST":
        bookingdata=tbl_Booking.objects.get(id=request.session["bookingid"])
        bookingdata.Booking_amount=request.POST.get("carttotalamt")
        bookingdata.Booking_status=1
        bookingdata.save()
        return redirect("User:booknow",request.session["bookingid"])
    else:
        bookcount = tbl_Booking.objects.filter(User_id=request.session["uid"],Booking_status=0).count()
        if bookcount > 0:
            book = tbl_Booking.objects.get(User_id=request.session["uid"],Booking_status=0)
            request.session["bookingid"] = book.id
            cart = tbl_Cart.objects.filter(Booking=book)
            return render(request,"User/Mypackage.html",{'package':cart})
        else:
            return render(request,"User/Mypackage.html")

def delpack(request,did):
   tbl_Cart.objects.get(id=did).delete()
   return redirect("User:mypackbooking")

def payment(request,id):
   booking = tbl_Booking.objects.get(id=id)
   amount = booking.Booking_amount
   if request.method == "POST":
      booking.Booking_status = 5
      booking.save()
      return redirect("User:loader")
   else:
      return render(request,"User/Payment.html", {"total":amount})

def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def mybooking(request):
    book = tbl_Booking.objects.filter(Booking_status__gt=1,User_id=request.session["uid"])
    return render(request,"User/Mybooking.html",{"booking":book})

def mybookpack(request, id):
    bookpack = tbl_Cart.objects.filter(Booking=id)
    return render(request, "User/MyBookPack.html", {"package":bookpack})

def ajaxserviceprovider(request):
    if request.GET.get("pid") != "":
        ser=tbl_Serviceprovider.objects.filter(sp_Place=request.GET.get("pid"))
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        for i in ser:
            tot=0
            ratecount=tbl_rating.objects.filter(servicerprovider=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(servicerprovider=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(ser,parry)
        return render(request, "User/Ajaxser.html",{"data":datas,"ar":ar})
    elif request.GET.get("did") != "":
        ser=tbl_Serviceprovider.objects.filter(sp_Place__district=request.GET.get("did"))
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        for i in ser:
            tot=0
            ratecount=tbl_rating.objects.filter(servicerprovider=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(servicerprovider=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(ser,parry)
        return render(request, "User/Ajaxser.html",{"data":datas,"ar":ar})
    else:
        ser=tbl_Serviceprovider.objects.all()
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        for i in ser:
            tot=0
            ratecount=tbl_rating.objects.filter(servicerprovider=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(servicerprovider=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(ser,parry)
        return render(request, "User/Ajaxser.html",{"data":datas,"ar":ar})
    
def custombooking(request,id):
    di=tbl_district.objects.all()
    packagetype=tbl_Packagetype.objects.all()
    sp=tbl_Serviceprovider.objects.get(id=id)
    if request.method=="POST":
        tbl_Custombooking.objects.create(Custombooking_todate=request.POST.get('date'),
                                         Place=tbl_place.objects.get(id=request.POST.get('sel_place')),
                                         Custombooking_description=request.POST.get('des'),
                                         User=tbl_User.objects.get(id=request.session["uid"]),
                                         Serviceprovider=tbl_Serviceprovider.objects.get(id=id),
                                         Packagetype=tbl_Packagetype.objects.get(id=request.POST.get("select_pack")))
        return redirect('User:viewservicerprofile',id)
    else:
        return render(request,'User/CustomizationBooking.html',{'district':di,"packaget":packagetype})
    
def mycustombooking(request):
    custom=tbl_Custombooking.objects.filter(User=request.session['uid'])
    return render(request,"User/MycustomizationBooking.html",{"custom":custom})

def customepayment(request, id):
    cus = tbl_Custombooking.objects.get(id=id)
    amount = cus.Custombooking_amount
    if request.method == "POST":
        cus.Custombooking_status = 4
        cus.save()
        return redirect("User:loader")
    return render(request,"User/Payment.html",{"total":amount})

def myticketbooking(request):
    ticket=tbl_Eventbooking.objects.filter(User_id=request.session['uid'])
    return render(request,"User/Myticketbooking.html",{"ticket":ticket})

def complaint(request):
    if request.method=="POST":
        tbl_Complaint.objects.create(Complaint_title=request.POST.get('title'),
                                     Complaint_content=request.POST.get('content'),
                                     User=tbl_User.objects.get(id=request.session["uid"]))
        return redirect('User:complaint')
    else:
        return render(request,'User/Complaint.html')
    
def viewreply(request):
    site = tbl_Complaint.objects.filter(User=request.session['uid'], package__isnull=True, Custombooking__isnull=True)
    booking = tbl_Complaint.objects.filter(User=request.session['uid'], package__isnull=False, Custombooking__isnull=True)
    custom = tbl_Complaint.objects.filter(User=request.session['uid'], package__isnull=True, Custombooking__isnull=False)
    return render(request,"User/ViewReply.html",{"site":site, "booking":booking, "custom":custom})

def packagecomplaint(request, id):
    if request.method=="POST":
        tbl_Complaint.objects.create(Complaint_title=request.POST.get('title'),
                                     Complaint_content=request.POST.get('content'),
                                     User=tbl_User.objects.get(id=request.session["uid"]),
                                     package=tbl_Addpackage.objects.get(id=id))
        return redirect('User:complaint')
    else:
        return render(request,'User/Complaint.html')

def customecomplaint(request, id):
    if request.method=="POST":
        tbl_Complaint.objects.create(Complaint_title=request.POST.get('title'),
                                     Complaint_content=request.POST.get('content'),
                                     User=tbl_User.objects.get(id=request.session["uid"]),
                                     Custombooking=tbl_Custombooking.objects.get(id=id))
        return redirect('User:complaint')
    else:
        return render(request,'User/Complaint.html')

def feedback(request):
    if request.method=="POST":
        tbl_Feedback.objects.create(Feedback_content=request.POST.get('txt_feedback'),user=tbl_User.objects.get(id=request.session["uid"]))
        return redirect('User:feedback')
    else:
        return render(request,"User/Feedback.html")
    
def rating(request,mid,name):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    if name == 1:
        counts=0
        counts=stardata=tbl_rating.objects.filter(organization=mid).count()
        if counts>0:
            res=0
            stardata=tbl_rating.objects.filter(organization=mid).order_by('-datetime')
            for i in stardata:
                res=res+i.rating_data
            avg=res//counts
            # print(avg)
            return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts,"name":name})
        else:
            return render(request,"User/Rating.html",{'mid':mid,"name":name})
    elif name == 2:
        counts=0
        counts=stardata=tbl_rating.objects.filter(servicerprovider=mid).count()
        if counts>0:
            res=0
            stardata=tbl_rating.objects.filter(servicerprovider=mid).order_by('-datetime')
            for i in stardata:
                res=res+i.rating_data
            avg=res//counts
            # print(avg)
            return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts,"name":name})
        else:
            return render(request,"User/Rating.html",{'mid':mid,"name":name})
    else:
        return render(request,"User/Rating.html",{'mid':mid,"name":name})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    if request.GET.get('name') == '1':
        tbl_rating.objects.create(user=tbl_User.objects.get(id=request.session["uid"]),user_review=user_review,rating_data=rating_data,organization=tbl_Organization.objects.get(id=pid))
        stardata=tbl_rating.objects.filter(organization=pid).order_by('-datetime')
        return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
    elif request.GET.get('name') == '2':
        tbl_rating.objects.create(user=tbl_User.objects.get(id=request.session["uid"]),user_review=user_review,rating_data=rating_data,servicerprovider=tbl_Serviceprovider.objects.get(id=pid))
        stardata=tbl_rating.objects.filter(servicerprovider=pid).order_by('-datetime')
        return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
    else:
        return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
    
def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    
    if request.GET.get('name') == '1':
        rate = tbl_rating.objects.filter(organization=request.GET.get("pdt"))
        ratecount = tbl_rating.objects.filter(organization=request.GET.get("pdt")).count()
        for i in rate:
            if int(i.rating_data) == 5:
                five = five + 1
            elif int(i.rating_data) == 4:
                four = four + 1
            elif int(i.rating_data) == 3:
                three = three + 1
            elif int(i.rating_data) == 2:
                two = two + 1
            elif int(i.rating_data) == 1:
                one = one + 1
            else:
                five = four = three = two = one = 0
            # print(i.rating_data)
            # r_len = r_len + int(i.rating_data)
        # rlen = r_len // 5
        # print(rlen)
        result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
        return JsonResponse(result)
    elif request.GET.get('name') == '2':
        rate = tbl_rating.objects.filter(servicerprovider=request.GET.get("pdt"))
        ratecount = tbl_rating.objects.filter(servicerprovider=request.GET.get("pdt")).count()
        for i in rate:
            if int(i.rating_data) == 5:
                five = five + 1
            elif int(i.rating_data) == 4:
                four = four + 1
            elif int(i.rating_data) == 3:
                three = three + 1
            elif int(i.rating_data) == 2:
                two = two + 1
            elif int(i.rating_data) == 1:
                one = one + 1
            else:
                five = four = three = two = one = 0
            # print(i.rating_data)
            # r_len = r_len + int(i.rating_data)
        # rlen = r_len // 5
        # print(rlen)
        result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
        return JsonResponse(result)
    else:
        return JsonResponse(result)
    
def ajaxamountfilter(request):
    if request.GET.get('amount') != "":
        pack = tbl_Addpackage.objects.filter(pack_amount__istartswith=request.GET.get("amount"))
        return render(request,"User/AjaxFilterAmount.html",{"pack": pack})
    else:
        pack = tbl_Addpackage.objects.filter(pack_spid=request.GET.get('servicer'))
        return render(request,"User/AjaxFilterAmount.html",{"pack": pack})