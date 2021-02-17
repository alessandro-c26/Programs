#This scraper uses a mix of Selenium and BeautifulSoup to navigate a site (a medical directory) and scrape a list of doctors.
#Only for explicative reasons, not to be used without the written consent of site owner.
#Confidential data like URLs and User's paths have been censored with a "@" sign.

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests 
from requests import get 
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np
import datetime
from random import randint

location_input = input("where?")

path_save = "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + "- " + location_input.replace(" ","") + ".csv"

driver = webdriver.Chrome()
driver.get("@@@@@@@@@@@@@@@@@@@@@@@@@@@")

driver.find_element_by_id("buttonPS").click()

pro_type = driver.find_element_by_name("ps_profession_label")
pro_type.send_keys("Médecin généraliste")
time.sleep(3)
pro_type.send_keys(Keys.ARROW_DOWN)
pro_type.send_keys(Keys.RETURN)

loc_type = driver.find_element_by_name("ps_localisation")
loc_type.send_keys(location_input)
time.sleep(3)
loc_type.send_keys(Keys.ARROW_DOWN)
loc_type.send_keys(Keys.ARROW_DOWN)
loc_type.send_keys(Keys.RETURN)

driver.find_element_by_class_name("bloc_submit").click()

time.sleep(randint(4,7))

html = driver.page_source

doc_name = []
address = []
cost = []
link = []

soup = BeautifulSoup(html, 'html.parser')
page_div = soup.find("div", class_="pagination")
last_page_soup = page_div.text
last_page = [int(s) for s in last_page_soup.split() if s.isdigit()]

pages = np.arange(1, last_page[0])

for pago in pages:

    soup = BeautifulSoup(html, 'html.parser')
     
    docto_div = soup.find_all("div", class_="item-professionnel")
    
    for docto_sing in docto_div: 
     
            name = docto_sing.h2.a.text 
            doc_name.append(name)

            link_url = docto_sing.find("a", href=True)
            name_fixed = name.strip().replace(" ","-").lower()
            link_url = link_url["href"].replace("recherche/fiche-detaillee-", "fiche-detaillee-" + name_fixed + "-")
            link_url = link_url.replace(".html", "")
            print(link_url)
            link.append("http://annuairesante.ameli.fr" + link_url)
    
            address_ind = docto_sing.find('div', class_="item left adresse").text 
            address.append(address_ind)
    
            cost_ind = docto_sing.find('div', class_="item right type_honoraires").text  
            cost.append(cost_ind)

    if pago + 1 <= last_page[0]:
        driver.get("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@" + str(pago + 1) + "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    
    time.sleep(randint(4,7))

    html = driver.page_source
    
docto_frame = pd.DataFrame({ 
'Doctor': doc_name, 'Address': address, 'Conventionné?': cost,'URL': link 
})

docto_frame.to_csv(path_save, sep=",", encoding="utf-16")

driver.quit()
