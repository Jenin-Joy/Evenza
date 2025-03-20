from django.urls import path,include
from Organization import views
app_name='Organization'
urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('Profile/',views.Profile,name='Profile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('Addevent/',views.Addevent,name='Addevent'),
    path('deleteevent/<int:eid>',views.deleteevent,name='deleteevent'),
    path('viewbooking/',views.viewbooking,name='viewbooking'),
    path('logout/',views.logout,name='logout'),
]