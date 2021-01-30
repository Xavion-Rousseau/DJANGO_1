
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class UHAUL_BOT:
    def __init__(self,Pickup,Dropoff,Pickup_Date):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.uhaul.com")
        action = ActionChains(self.driver)
        
        self.driver.find_element_by_xpath("//input[@name='PickupLocation']").send_keys(Pickup)
        self.driver.find_element_by_xpath("//input[@name='DropoffLocation']").send_keys(Dropoff)
        self.driver.find_element_by_xpath("//input[@name='PickupDate']").send_keys(Pickup_Date)
        action.send_keys(Keys.ESCAPE)
        action.perform()
        action.send_keys(Keys.ENTER)
        action.perform()
        #self.driver.find_element_by_xpath("//*[@id='mpBody']").send_keys(Keys.ESCAPE) 
        #self.driver.find_element_by_xpath("//button[@type='submit']").click()
        sleep(5)
    def get_truck_10(self):
        self.driver.find_element_by_xpath("//*[@id='submit_TM']").click()
class MapScrape:
    def __init__(self,Pickup,Dropoff,Pickup_Date):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/maps/@33.005102,-96.5493228,11z')  
        
