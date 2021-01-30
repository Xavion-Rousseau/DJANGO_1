import requests
import re
import usaddress
from itertools import chain 
from .models import Email,Estiment
from .form import EmailForm, EstimentForm

class WhatService:
        def min_rate(request):
            if request.method == 'POST':
                if request.POST['Storage_Estiment']:
                    labor_chrarge = {'price':'$0.99 per labor min'}
                if request.POST['Home_Move_Estiment']:
                    labor_chrarge = {'price':'$0.99 per labor min'}
                if request.POST['Donation_Estiment']:
                    labor_chrarge = {'price':'$0 per labor min'}
                if request.POST['Junk_Estiment']:
                    labor_chrarge = {'price':'$1 per labor min'}
            return labor_chrarge

                    