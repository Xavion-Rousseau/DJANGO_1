from django import forms
from .models import Booked,Email,Estiments_People,Estiments_Truck,Estiments_Services,Estiments_Locations


class Esti_service(forms.ModelForm):
    class Meta:
        model = Estiments_Services
        fields = ['Storage_Estiment', 'Home_Move_Estiment','Donation_Estiment','Junk_Estiment','Pickups_Estiment','Craiglist_Estiment']
class Esti_LocForm(forms.ModelForm):
    class Meta:
        model = Estiments_Locations
        fields = ['pickup_location','dropoff_location']

class Esti_peopleForm(forms.ModelForm):
    class Meta:
        model = Estiments_People
        fields = ['one_people','two_people']   
class Esti_TruckFrom(forms.ModelForm):
    class Meta:
        model = Estiments_Truck
        fields = ['pickup','ten_truck','fifteen_truck','seventeen_truck','twenty_truck','twenty_six_truck']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['name_Email','email_Email','message_Email']
        
class BookedForm(forms.ModelForm):
    class Meta:
        model = Booked
        fields = ['Name','phone_number','date','time','details','book_service','book_truck','book_crew']