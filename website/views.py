from django.shortcuts import render
from django.core.mail import send_mail
from .models import Booked,Email,Estiments_People,Estiments_Truck,Estiments_Services,Estiments_Locations

from .form import Esti_service,Esti_LocForm,Esti_peopleForm,Esti_TruckFrom,EmailForm,BookedForm

from .Distance import Map

#from .Distance import Map

# Create your views here.
#from .form import MemberForm


def home(request):
    if request.method == 'POST':
        dic = {}
        
        if 'date' in request.POST:
            dic['date']=request.POST['date']
            dic['time']=request.POST['time']
            dic['service']= request.POST['book_service']
            dic['truck']=request.POST['book_truck']
            dic['crew']= request.POST['book_crew']
            return render(request,'home.html',dic)
    return render(request,'home.html',{})

def Estiment(request):
    if request.method == 'POST':
        dic = {}
        
        if 'date' in request.POST:
            dic['date']=request.POST['date']
            dic['time']=request.POST['time']
            dic['service']= request.POST['book_service']
            dic['truck']=request.POST['book_truck']
            dic['crew']= request.POST['book_crew']
            return render(request,'home.html',dic)
        
        # STARTS TO CHECK FORMS
        
        if 'Storage_Estiment' in request.POST:
            dic['service'] = request.POST['Storage_Estiment']
            dic['Labour'] = '$0.99/labour min'

        elif 'Home_Move_Estiment' in request.POST:
            
            dic['service'] = request.POST['Home_Move_Estiment']
            dic['Labour'] = '$0.99/labour min'
            
        elif 'Donation_Estiment' in request.POST:
            dic['service'] = request.POST['Donation_Estiment']
            dic['Labour'] = '$0.99/labour min'
            
        elif 'Junk_Estiment' in request.POST:
            dic['service'] = request.POST['Junk_Estiment']
            dic['Labour'] = '$1.99/labour min'
            
        elif 'Pickups_Estiment' in request.POST:
            dic['service'] = request.POST['Pickups_Estiment']
            dic['Labour'] = '$2.99/labour min'
            
        elif 'Craiglist_Estiment' in request.POST:
            dic['service'] = request.POST['Craiglist_Estiment']
            dic['Labour'] = '$1.99/labour min'
        # FORM FOR TRUCKS
        if 'pickup' in request.POST:
            dic['truck'] = request.POST['pickup']
            dic['miles'] = '$24.99 + $1.99/mile'
            multi = 1.99
            plus = 24.99
        elif 'ten_truck' in request.POST:
            dic['truck'] = request.POST['ten_truck']
            dic['miles'] = '$39.99 + $1.99/mile'
            multi = 1.99
            plus = 39.99
        elif 'fifteen_truck' in request.POST:
            dic['truck'] = request.POST['fifteen_truck']
            dic['miles'] = '$49.99 + $1.99/mile'
            multi = 1.99
            plus = 49.99
        elif 'seventeen_truck' in request.POST:
            dic['truck'] = request.POST['seventeen_truck']
            dic['miles'] = '$149.99 + $3.99/mile'
            multi = 3.99
            plus = 149.99
        elif 'twenty_truck' in request.POST:
            dic['truck'] = request.POST['twenty_truck']
            dic['miles'] = '$249.99 + $4.99/mile'
            multi = 4.99
            plus = 249.99
        elif 'twenty_six_truck' in request.POST:
            dic['truck'] = request.POST['twenty_six_truck']
            dic['miles'] = '$449.99 + $4.99/mile'
            multi = 4.99
            plus = 499.99


        # FORM FOR CREW
        if 'one_peolpe' in request.POST:
            dic['crew'] = request.POST['one_people']
        elif 'two_people' in request.POST:
            dic['crew'] = request.POST['two_people']
            
        #LOCATION DICTIONS TO PASS TO JINJA and my range finding func
        pickup_location = request.POST['pickup_location']
        dropoff_location =request.POST['dropoff_location']
        location_dic = {'pickup_location':pickup_location, 'dropoff_location':dropoff_location}
        dic.update(location_dic)  
        string_pickup = str(dic.get('pickup_location'))
        string_dropoff = str(dic.get('dropoff_location'))
        MAP = Map(string_pickup,string_dropoff)
        are_range = MAP.find_range(string_pickup,string_dropoff)
        if are_range == True:
            dic['total'] = str(MAP.find_miles_price(multi,plus))
            
            return render(request,'Estiment.html',dic)
        elif are_range == False:
            false_dic = {'no':'noo'}
            return render(request,'Estiment.html',false_dic)

    #if not post
    return render(request,'Estiment.html')


