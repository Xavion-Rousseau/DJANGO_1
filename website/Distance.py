import requests
import re
import usaddress
from itertools import chain 
import math
import os
from decouple import config


URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'

class Map:
    def __init__(self,pickup,dropoff):

        #URL FOR GOOGLE API base
        URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&'

        #URL FOR GOOGLE API base
        

        #API_KEY FOR GEO,PLACES,MATRIX, and 
        self.API_KEY = config('API_KEY')

        self.request = requests.get(URL + "origins=" + pickup + "&destinations=" + dropoff + "&key=" + self.API_KEY)

    def find_range(self,pickup,dropoff):
        
        MY_LOCATION = '33.119480,-96.625930'
        
        #RANGE OF PICKUP COORD FROM ME
        range_of_pickup =requests.get(URL + "origins=" + MY_LOCATION + "&destinations=" + pickup + "&key=" + self.API_KEY)
        range_found_pickup = range_of_pickup.json()['rows'][0]['elements'][0]['distance']['text']
        #print(range_found_pickup)
        #RANGE OF DROP OFF COORD FROM ME 
        range_of_drop = requests.get(URL + "origins=" + MY_LOCATION + "&destinations=" + dropoff + "&key=" + self.API_KEY)
        range_found_drop = range_of_drop.json()['rows'][0]['elements'][0]['distance']['text']
        #print(range_found_drop)
        # Want to make sure we don pass up a potential move in the 1500 mile + range 
        range_of_move = requests.get(URL + "origins=" + pickup + "&destinations=" + dropoff + "&key=" + self.API_KEY)
        range_found_move = range_of_move.json()['rows'][0]['elements'][0]['distance']['text']
        #print(range_found_move)
        range_foundM = range_found_move.replace(',','')
        range_found = range_foundM.replace('mi','')

        
        
        #checking of drop off or pick upp are in ft and are not 100 away from me
        pattern = re.compile(r"ft")
        if pattern.findall(range_found_pickup) or pattern.findall(range_found_drop) or pattern.findall(range_found_move) :
            s = range_found_move.replace('mi','')
            n= s.replace(',','')
            if int(float(s)) < 100:
                return True
                
        
        if int(float(range_found)) > 1700:
            return True
        s = range_found_pickup.replace('mi','')
        n= range_found_drop.replace('mi','')
        if int(float(s)) < 100 or int(float(n)) < 100:
            return True 

        return False 
            


    def find_miles_price(self,times,plu):

        distance = self.request.json()['rows'][0]['elements'][0]['distance']['text']

        #removing letters to multiply for client estiment
        remove_letter = re.sub(r'mi|ft','',distance)
        
        e = ''.join(map(str,remove_letter))

        #int_mile = int(float(miles))
        miles = e.replace(',','')
        
        return round(int(float(miles)) * times + plu,2)

ma = Map('California, USA','Florida, USA')
ma.find_range('California, USA','Florida, USA')