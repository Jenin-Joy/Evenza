from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *

# Create your views here.
def index(request):
    return render(request,'Guest/index.html.')

def Serviceprovider(request):
    di=tbl_district.objects.all()
    sp=tbl_Serviceprovider.objects.all()
    if request.method=="POST":
        tbl_Serviceprovider.objects.create(sp_Name=request.POST.get('name'),sp_Gmail=request.POST.get('mail'),
                                           sp_Contact=request.POST.get('num'),sp_Address=request.POST.get('add'),
                                           sp_Place=tbl_place.objects.get(id=request.POST.get('sel_place')),
                                           sp_Password=request.POST.get('pass'),sp_Photo=request.FILES.get("photo"),
                                           sp_Proof=request.FILES.get("proof"))
        return redirect('Guest:Serviceprovider')
    else:
        return render(request,'Guest/Serviceprovider.html',{'district':di,'Serviceprovider':sp})

def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get('did'))
    return render(request,'Guest/AjaxPlace.html',{'place':place})

def user(request):
    us=tbl_User.objects.all()
    if request.method=="POST":
        tbl_User.objects.create(user_Name=request.POST.get('name'),user_Email=request.POST.get('mail'),
                                user_Contact=request.POST.get('num'),user_Address=request.POST.get('add'),
                                user_Password=request.POST.get('pass'))
        return redirect('Guest:user')
    else:
        return render(request,'Guest/User.html',{'user':us})

def Organization(request):
    di=tbl_district.objects.all()
    org=tbl_Organization.objects.all()
    if request.method=="POST":
        tbl_Organization.objects.create(org_Name=request.POST.get('name'),org_Email=request.POST.get('mail'),
                                        org_Contact=request.POST.get('num'),org_Address=request.POST.get('add'),
                                        org_Place=tbl_place.objects.get(id=request.POST.get('sel_place')),
                                        org_Logo=request.FILES.get("logo"),org_Proof=request.FILES.get("proof"),
                                        org_Password=request.POST.get('pass'),)
        return redirect('Guest:Organization')
    else:
        return render(request,'Guest/Organization.html',{'Organization':org,'district':di})
    
def login(request):
    if request.method=="POST":
        admincount=tbl_AdminRegistration.objects.filter(Mail=request.POST.get('mail'),Password=request.POST.get('pass')).count()
        usercount=tbl_User.objects.filter(user_Email=request.POST.get('mail'),user_Password=request.POST.get('pass')).count()
        spcount=tbl_Serviceprovider.objects.filter(sp_Gmail=request.POST.get('mail'),sp_Password=request.POST.get('pass')).count()
        orgcount=tbl_Organization.objects.filter(org_Email=request.POST.get('mail'),org_Password=request.POST.get('pass')).count()

        if admincount > 0:
            admin=tbl_AdminRegistration.objects.get(Mail=request.POST.get('mail'),Password=request.POST.get('pass'))
            request.session['aid']=admin.id
            return redirect('Admin:homepage')
        elif usercount > 0:
            user=tbl_User.objects.get(user_Email=request.POST.get('mail'),user_Password=request.POST.get('pass'))
            request.session['uid']=user.id
            return redirect('User:homepage')
        elif orgcount > 0:
            org=tbl_Organization.objects.get(org_Email=request.POST.get('mail'),org_Password=request.POST.get('pass'))
            if org.org_Status == "0":
                return render(request,'Guest/login.html',{'msg':'Your Registration is Pending'})
            elif org.org_Status == "2":
                return render(request,'Guest/login.html',{'msg':'Your Registration is Rejected'})
            else:
                request.session['oid']=org.id
                return redirect('Organization:homepage')
        elif spcount > 0:
            sp=tbl_Serviceprovider.objects.get(sp_Gmail=request.POST.get('mail'),sp_Password=request.POST.get('pass'))
            if sp.sp_Status == 0:
                return render(request,'Guest/login.html',{'msg':'Your Registration is Pending'})
            elif sp.sp_Status == 2:
                return render(request,'Guest/login.html',{'msg':'Your Registration is Rejected'})
            else:
                request.session['spid']=sp.id
                return redirect('Serviceprovider:homepage')
        else:
            return render(request,'Guest/login.html',{'msg':'Invalid'})
    else:
        return render(request,'Guest/login.html')
    
