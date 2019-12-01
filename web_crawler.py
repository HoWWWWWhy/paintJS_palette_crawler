#import requests

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
from selenium import webdriver
import time
import re# 정규식

chrome_driver_path = "./chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome(
    executable_path = chrome_driver_path
)    
URL = "https://flatuicolors.com"
driver.get(URL)
#time.sleep(1)

html = driver.page_source

# reference: https://medium.com/@speedforcerun/python-crawler-http-error-403-forbidden-1623ae9ba0f
# Using urllib.request.urlopen() to open a website when crawling, and encounters “HTTP Error 403: Forbidden”.
# It possibly due to the server does not know the request is coming from. 
# Some websites will verify the UserAgent in order to prevent from abnormal visit. 
# So you should provide information of your fake browser visit.
#headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

#req = Request(url=URL, headers=headers)
#html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

small_palettes = soup.find_all('a','smallpalette-container')
print(len(small_palettes))
total_palettes = []

p = re.compile('rgb\(\d*, \d*, \d*\)')# 추출형태: (r, g, b)

for small_palette in small_palettes:
    colors = list(small_palette.children)    
    cur_palette_name = colors[0].find('div', {'class' :'name'}).text
    print(cur_palette_name)

    color_list = list(colors[0].children)
    cur_palette = []    
    for color in color_list:
        rgb = p.findall(str(color))
        if(rgb):
            cur_palette += rgb
        
    print(cur_palette)
    #total_palettes += cur_palette

#print(total_palettes)
driver.close()
