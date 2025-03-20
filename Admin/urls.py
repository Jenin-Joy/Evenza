from django.urls import path,include
from Admin import views
app_name='Admin'
urlpatterns = [
    path('District/',views.District,name='District'),
    path('AdminRegistration/',views.AdminRegistration,name='AdminRegistration'),
    path('Eventtype/',views.Eventtype,name='Eventtype'),
    path('place/',views.place,name='place'),
    path('deletedistrict/<int:did>',views.deletedistrict,name='deletedistrict'),
    path('deleteadmin/<int:aid>',views.deleteadmin,name='deleteadmin'),
    path('deleteevent/<int:eid>',views.deleteevent,name='deleteevent'),
    path('editdistrict/<int:did>',views.editdistrict,name='editdistrict'),
    path('editadmin/<int:aid>',views.editadmin,name='editadmin'),
    path('editevent/<int:eid>',views.editevent,name='editevent'),
    path('deleteplace/<int:pid>',views.deleteplace,name='deleteplace'),
    path('editplace/<int:pid>',views.editplace,name='editplace'),
    path('homepage/',views.homepage,name='homepage'),
    path('Packagetype/',views.Packagetype,name='Packagetype'),
    path('deletepackage/<int:pid>',views.deletepackage,name='deletepackage'),
    path('editpackage/<int:pid>',views.editpackage,name='editpackage'),
    path('viewcomplaint/',views.viewcomplaint,name='viewcomplaint'),
    path('reply<int:id>/',views.reply,name='reply'),
    path('replyedcomplaint/',views.replyedcomplaint,name='replyedcomplaint'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),

    path('neworganization/',views.neworganization,name="neworganization"),
    path('newserviceprovider/',views.newserviceprovider,name="newserviceprovider"),

    path('acceptedorganization/',views.acceptedorganization,name="acceptedorganization"),
    path('acceptedserviceprovider/',views.acceptedserviceprovider,name="acceptedserviceprovider"),

    path('rejectedorganization/',views.rejectedorganization,name="rejectedorganization"),
    path('rejectedserviceprovider/',views.rejectedserviceprovider,name="rejectedserviceprovider"),
    path('logout/',views.logout,name="logout"),

    path('verifyorganization/<int:id>/<int:status>',views.verifyorganization,name="verifyorganization"),
    path('verifyserviceprovider/<int:id>/<int:status>',views.verifyserviceprovider,name="verifyserviceprovider"),
]
