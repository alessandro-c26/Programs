import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
from random import randint
from numpy.core.defchararray import strip
import datetime

ricette = []
descrizioni = []
difficolta_list = []
portata_list = []
thematics_list = []

path = "/Users/alessandrocarletta/Desktop/Python/My Code/ricette.csv"

pages = np.arange(1, 100)
portata = ["Antipasti", "Primi", "Secondi-piatti", "Contorni", "Lievitati", "Piatti-Unici"]
thematics = ["Pesce", "Vegetariani"]

print("starting scraping at...", datetime.datetime.now())

for porta in portata:
  for theme in thematics:
    for page in pages:

      pagede = requests.get("https://www.giallozafferano.it/ricette-cat/page" + str(page) + "/" + str(porta) + "/" + str(theme))

      soup = BeautifulSoup(pagede.text, 'html.parser')
      ricette_div = soup.find_all("div", class_="gz-content-recipe-horizontal")

      for ricetta_soup in ricette_div:

        name = ricetta_soup.h2.a.text
        ricette.append(name)

        descrizione = ricetta_soup.find('div', class_='gz-description').text
        descrizioni.append(descrizione)

        difficolta = ricetta_soup.find('div', class_="gz-col-flex gz-double gz-mTop10").text[25:37]
        difficolta_list.append(strip(difficolta))

        portata_list.append(porta)
        thematics_list.append(theme)

      #sleep(randint(2,7))
  print("nuova portata...", datetime.datetime.now())

ricette = pd.DataFrame({
'Ricetta': ricette, 'Descrizione': descrizioni, 'Difficoltà': difficolta_list, 'Portata': portata_list, 'Tipo': thematics_list
})

ricette.head()

ricette.to_csv(path, sep=",", encoding="utf-16")