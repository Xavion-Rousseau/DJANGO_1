from django import forms
from .models import Email,Estiment

class EstimentForm(forms.ModelForm):
    class Meta:
        model = Estiment
        fields = ['Storage_Estiment', 'Home_Move_Estiment','Donation_Estiment','Junk_Estiment','Pickups_Estiment','Craiglist_Estiment','pickup','ten_truck','fifteen_truck','seventeen_truck','twenty_truck','twenty_six_truck','one_peolpe','two_people','pickup_location','dropoff_location','Name','phone_number','date','time','details','book_service','book_truck','book_crew']        
class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('name_Email','email_Email','message_Email')

