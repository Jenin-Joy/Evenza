from django.urls import path,include
from Guest import views
app_name='Guest'
urlpatterns = [
    path('Serviceprovider/',views.Serviceprovider,name='Serviceprovider'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('User/',views.user,name='user'),
    path('Organization/',views.Organization,name='Organization'),
    path('login/',views.login,name='login'),
    path('',views.index,name='index'),
]
