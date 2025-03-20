from django.urls import path,include
from User import views
app_name='User'

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('Profile/',views.Profile,name='Profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('viewsp/',views.viewsp,name='viewsp'),
    path('viewservicerprofile/<int:spid>',views.viewservicerprofile,name='viewservicerprofile'),
    path('viewpackage/<int:pid>',views.viewpackage,name='viewpackage'),
    path('viewwork/<int:wid>',views.viewwork,name='viewwork'),
    path('booknow/<int:id>',views.booknow,name='booknow'),
    path('viewgallery/',views.viewgallery,name='viewgallery'),
    path('viewevent/',views.viewevent,name='viewevent'),
    path('bookcount/<int:id>',views.bookcount,name='bookcount'),
    path("ticketpayment/<int:id>",views.ticketpayment,name="ticketpayment"),
    path('Addcart/<int:pid>/<int:id>',views.Addcart, name='Addcart'),
    path('mypackbooking/',views.mypackbooking, name='mypackbooking'),
    path("delpack/<int:did>", views.delpack,name="delpack"),
    path("payment/<int:id>",views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path('mybooking/',views.mybooking, name='mybooking'),
    path('mybookpack/<int:id>',views.mybookpack, name='mybookpack'),
    path('ajaxserviceprovider/',views.ajaxserviceprovider, name='ajaxserviceprovider'),
    path('custombooking/<int:id>',views.custombooking,name='custombooking'),
    path('mycustombooking/',views.mycustombooking,name='mycustombooking'),
    path('customepayment/<int:id>',views.customepayment,name='customepayment'),
    path('myticketbooking/',views.myticketbooking,name='myticketbooking'),
    path('complaint/',views.complaint,name='complaint'),
    path('viewreply/',views.viewreply,name='viewreply'),
    path('feedback/',views.feedback,name='feedback'),

    path('rating/<int:mid>/<int:name>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('ajaxamountfilter/',views.ajaxamountfilter,name="ajaxamountfilter"),
    path('logout/',views.logout,name="logout"),
    path('packagecomplaint/<int:id>',views.packagecomplaint,name="packagecomplaint"),
    path('customecomplaint/<int:id>',views.customecomplaint,name="customecomplaint"),
]