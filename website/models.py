from django.db import models
from django.utils import timezone

class Estiments(models.Model):
    Storage_Estiment = models.BooleanField(default=False)	
    Home_Move_Estiment = models.BooleanField(default=False)	
    Donation_Estiment = models.BooleanField(default=False)	
    Junk_Estiment = models.BooleanField(default=False)	
    Pickups_Estiment = models.BooleanField(default=False)	
    Craiglist_Estiment = models.BooleanField(default=False)	
    pickup= models.BooleanField(default=False)
    ten_truck= models.BooleanField(default=False)
    fifteen_truck= models.BooleanField(default=False)
    seventeen_truck= models.BooleanField(default=False)
    twenty_truck= models.BooleanField(default=False)
    twenty_six_truck= models.BooleanField(default=False)
    one_peolpe= models.BooleanField(default=False)
    two_people = models.BooleanField(default=False)	
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    Name = models.CharField(max_length=255)
    phone_number= models.IntegerField()
    date=models.DateField(default=timezone.now)
    time=models.TimeField()
    details = models.CharField(max_length=255)
    book_service= models.CharField(max_length=255)
    book_truck=models.CharField(max_length=255)
    book_crew=models.CharField(max_length=255)






class Email(models.Model):

    name_Email = models.CharField(max_length=100)
    email_Email = models.EmailField(max_length=100)
    message_Email = models.CharField(max_length=500)
   


    