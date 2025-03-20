from django.urls import path,include
from Serviceprovider import views
app_name='Serviceprovider'
urlpatterns = [
    path('Addpackage/',views.Addpackage,name='Addpackage'),
    path('deletepackage/<int:pid>',views.deletepackage,name='deletepackage'),
    path('homepage/',views.homepage,name='homepage'),
    path('Profile/',views.Profile,name='Profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    
    path('addwork/',views.addwork,name='addwork'),
    path('deletework/<int:id>',views.deletework,name='deletework'),
    path('gallery/<int:id>',views.gallery,name='gallery'),
    path('deletegallery/<int:id>/<int:workid>',views.deletegallery,name='deletegallery'),
    path('viewcustombooking/',views.viewcustombooking,name='viewcustombooking'),
    path('viewpackagebooking/',views.viewpackagebooking,name='viewpackagebooking'),
    path('bookingstatus/<int:bid>/<int:value>',views.bookingstatus,name='bookingstatus'),

    path('updatecustom/<int:id>/<int:status>',views.updatecustom,name='updatecustom'),
    path('ajaxaddamount/',views.ajaxaddamount,name='ajaxaddamount'),
    path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('reply/<int:id>',views.reply,name='reply'),
    path('replyedcomplaint/',views.replyedcomplaint,name='replyedcomplaint'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('logout/',views.logout,name='logout'),
]
