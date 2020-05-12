#This program creates a WordCloud from a Wikipedia Page (Input URL must be from a Wikipedia article)
#created by alessandro c. - only available for personal uses

from bs4 import BeautifulSoup
import nltk
import requests 
import re
import numpy as np
import pandas as pd
import os
from PIL import Image
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from numpy import unicode

url = input("Enter URL: ")
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')

main_content = soup.find("div", attrs= {"id" : "mw-content-text"})
lists = main_content.find_all("li")

str = ""
for list in lists:
    info= list.text
    str+=info

STOPWORDS.add("https")
STOPWORDS.add("ISBN")
STOPWORDS.add("co")
STOPWORDS.add("Archived")
STOPWORDS.add("Original")
STOPWORDS.add("RT")
STOPWORDS.add("Retrieved")
STOPWORDS.add("PDF")
STOPWORDS.add("pp")
stopwords = set(STOPWORDS)

cloud = WordCloud(
    background_color='white', 
    width=800, 
    height=400,
    max_words=200,
    stopwords=stopwords
).generate(str)

fig = plt.figure()
fig.set_figwidth(20)
fig.set_figheight(20)

plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
