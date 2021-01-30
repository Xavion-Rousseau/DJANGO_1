
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('Cities.html',views.Cities,name="Cities"),
   path('Services.html',views.Services,name="Services"),
   path('Estiment.html',views.Estiment,name="Estiment"),
   path('house.html',views.house,name="house"),
   path('Delivery.html',views.Delivery,name="Delivery"),
   path('donation.html',views.donation,name="donation"),
   path('Storage.html',views.Storage,name="Storage"),
   path('junk.html',views.junk,name="junk"),
   path('craiglist',views.craiglist,name="craiglist"),
   path('Custoz.html',views.Custoz,name="Custoz"),
   path('Trucks.html',views.Trucks,name="Trucks"),
   path('Booking.html',views.Booking,name="Booking"),
]
