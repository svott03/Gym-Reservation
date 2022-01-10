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
  sleep(3)
  
  self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[1]/div/div[3]/p/a').click()
  sleep(3)
  while True:
    html_text = self.driver.page_source
    soup = BeautifulSoup(html_text, 'lxml')
    #extract div
    mydivs = soup.find_all("div", class_="booking-slot-item")
    #iterate through divs
    for div in mydivs:
        #div str text
        temp = div.get_text()
        #if your time is available
        if "1:15 - 3:15 PM" in temp:
            #extracts text
            textLine = div.find('span')
            result = textLine.get_text().strip()
            #checks spots available
            if not "No spots available" in result:
                #sends phone msg
                account_sid = 'sid'
                auth_token = 'token'
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
#instantiates object
page = Google(username,password)
