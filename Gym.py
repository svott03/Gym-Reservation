from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import os
from twilio.rest import Client


class Google:

 def __init__(self,username,password):
  self.driver=webdriver.Safari(executable_path='/usr/bin/safaridriver')
  #sets up driver and passes login
  self.driver.get('https://myrecsports.usc.edu/booking/cd93ade2-af9d-4e5f-84e0-06e10711b5ce')
  sleep(3)
  self.driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button').click()
  sleep(4)
  self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
  self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
  self.driver.find_element_by_xpath('//*[@id="loginform"]/div/button').click()
  sleep(5)
  
  self.driver.switch_to.frame(self.driver.find_element_by_id("duo_iframe"))
  self.driver.find_element_by_xpath('//*[@id="passcode"]').click()
  sleep(4)
  self.driver.find_element_by_xpath('//*[@id="auth_methods"]/fieldset/div[3]/div/input').send_keys(duo)
  self.driver.find_element_by_xpath('//*[@id="passcode"]').click()
  sleep(3)
  
  sleep(3)
  count = 0
  self.driver.get("https://myrecsports.usc.edu/booking/cd93ade2-af9d-4e5f-84e0-06e10711b5ce")
  while True:
    #self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="divBookingSlots"]/div[2]/div[1]'))
    html_text = self.driver.page_source
    #html_text = "https://myrecsports.usc.edu/booking/cd93ade2-af9d-4e5f-84e0-06e10711b5ce"
    #html_text = url.page_source
    print(f"TEST{count}")
    count+=1
    soup = BeautifulSoup(html_text, 'lxml')
    #extract div
    mydivs = soup.find_all("div", class_="booking-slot-item")
    #iterate through divs
    for div in mydivs:
        #div str text
        temp = div.get_text()
        #if your time is available
        if "8:30 - 10:30 PM" in temp:
            #extracts text
            textLine = div.find('span')
            result = textLine.get_text().strip()
            #checks spots available
            if not "No spots available" in result:
                #sends phone msg
                account_sid = 'account_sid'
                auth_token = 'auth_token'
                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                        to='phone_number',
                        from_="+12135681813",
                        body = "Gym Spot Available"
                    )
                print(result)
                quit()
                break

    
    sleep(2)
    self.driver.refresh()
    sleep(3)

#for username and password privacy
user=open('New Text Document (3).txt',"r",encoding="utf-8")   
username=str(user.read())
passw=open('New Text Document (2).txt',"r",encoding="utf-8")   
password=str(passw.read())
duo = duo_password
#instantiates object
page = Google(username,password)
