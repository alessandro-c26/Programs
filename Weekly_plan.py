# This program uses the output of webscraper.py to create a casual weekly table of recipes to prepare.
# It continues generating weekly plans until the user types "Y". When this happens, the program outputs an excel and a list.
# Sensible data has been censored with an "@" sign 

import pandas as pd
import random
import datetime
from random import randint
from random import randrange
from requests.api import head

path_to_read = "@@@@@@@@@@@@@@@@@@@@@@@"
df = pd.read_csv(path_to_read, sep=",", encoding="utf-8-sig")
df.drop(columns=["Unnamed: 0"], inplace=True)

decision_variable = "N"
good_result = "Y"

while decision_variable != good_result: 

    meals = 7
    numbers = []
    to_save = []
    url_list = []
    
    day = int(0)

    while len(numbers) < meals:
        number = randrange(0,2357, 1)
        numbers.append(number)

    columns = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    index = ["Lunch", "Dinner"]

    df2 = pd.DataFrame(columns = columns, index=index)
    df3 = pd.DataFrame()

    for number in numbers:
        df3 = df3.append(df.iloc[number])
        url_list.append("https://ricette.@@@@@@@@@@@@.it/" + df.iloc[number, 1].replace(" ","-").replace(",","").replace("®","").replace("'","-") + ".html")
        
        df2.loc[random.choice(index), columns[day]] = df.iloc[int(number), 1]
        day = int(day) + 1

    df_final = df3.drop(columns=["Unnamed: 0.1"])
    df_final["URL"] = url_list

    print(df2)
    print(df_final)

    decision_variable = input("Do you like it? Y/N...").upper()    

time = str(datetime.datetime.now().isocalendar()[1]).strip()
hour = str(datetime.datetime.now().hour)
minute = str(datetime.datetime.now().minute)
second = str(datetime.datetime.now().second)

path_export1 = "/Users/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/Schedule - week " + time + " - " + hour + "h" + minute + ".csv"
path_export2 = "/Users/@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/New/List - week " + time + " - " + hour + "h" + minute + ".csv"

df2.to_csv(path_export1, encoding="utf-8-sig")
df_final.to_csv(path_export2, encoding="utf-8-sig")
