#!/usr/bin/env python
# coding: utf-8

# In[85]:


# pip install webdriver-manager


# In[86]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
import time
from pathlib import Path

source_fk = "https://www.flipkart.com/apple-iphone-13-starlight-128-gb/p/itmc9604f122ae7f?pid=MOBG6VF5ADKHKXFX&lid=LSTMOBG6VF5ADKHKXFXZVXGTL&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&srno=s_1_4&otracker=search&otracker1=search&fm=Search&iid=d8dee1c3-72a3-4481-9983-57b1f770895b.MOBG6VF5ADKHKXFX.SEARCH&ppt=sp&ppn=sp&ssid=do6adf98e80000001658300206266&qH=c68a3b83214bb235"
source_az = "https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/ref=sr_1_2_sspa?crid=ANTLHWBAABCW&keywords=iphone+13+pro&qid=1658300147&sprefix=iphone+13+pro%2Caps%2C267&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNUFVSk1HQUdZQjVHJmVuY3J5cHRlZElkPUEwNTEzNzI0M05URlEyTVpXOVIwUCZlbmNyeXB0ZWRBZElkPUEwMzMzNDIwMUxMVFRKWjlXSkhKUSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
#source_az_logged = "https://www.amazon.in/Apple-iPhone-13-128GB-Starlight/dp/B09G9D8KRQ/ref=sr_1_3?crid=16T97A3M26WEA&keywords=iphone+13&qid=1658300601&sprefix=iphone+13%2Caps%2C605&sr=8-3"

print(source_fk)
print(source_az)
# print(source_cr)


# In[98]:


# create a webdriver object for chrome-option and configure
wait_imp = 10
CO = webdriver.ChromeOptions()
CO.add_experimental_option('useAutomationExtension', False)
CO.add_argument('--ignore-certificate-errors')
CO.add_argument('--start-maximized')

## Manually upload the latest chromedriver.exe file onto the anaconda path folder
# wd = webdriver.Chrome(r'chromedriver.exe',options=CO)

## Automatically picks up and installs the latest chromedriver.exe file from internet
wd = webdriver.Chrome(ChromeDriverManager().install(), options=CO)

print ("*************************************************************************** \n")
print("                     Starting Program, Please wait ..... \n")


### FLIPKART DATA RETRIEVAL
print ("Connecting to Flipkart")
wd.get(source_fk)

source_fk_price_xpath = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
source_fk_price = source_fk_price_xpath.text

source_fk_prod_xpath = wd.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
product_name = source_fk_prod_xpath.text

print (" ---> Successfully retrieved the price from Flipkart \n")
time.sleep(2)


### AMAZON DATA RETRIEVAL
print ("Connecting to Amazon")
wd.get(source_az)

source_az_price_xpath = wd.find_element_by_xpath("/html/body/div[4]/div[2]/div[3]/div[11]/div[15]/div[1]/div[1]/span[2]/span[2]/span[2]")
source_az_price = source_az_price_xpath.text

source_az_prod_xpath = wd.find_element_by_xpath("/html/body/div[4]/div[2]/div[3]/div[11]/div[3]/div/h1/span")
product = source_az_prod_xpath.text

print (" ---> Successfully retrieved the price from Amazon \n")
time.sleep(2)


# Final display
print ("#------------------------------------------------------------------------#")
print ("Price for [{}] on all websites, Prices are in INR \n".format(product))
print("Price available at Flipkart is: "+source_fk_price[1:])
print("Price available at Amazon is: "+source_az_price[0:])


# In[ ]:




