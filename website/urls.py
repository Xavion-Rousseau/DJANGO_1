
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home,name="home"),
   path('Estiment.html',views.Estiment,name="Estiment"),
]
