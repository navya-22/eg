from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import chromedriver_binary
from urllib.request import urlopen
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium import webdriver as selenium_webdriver
import time
from selenium.webdriver.chrome.service import Service 
import pandas as pd 
from selenium.webdriver.common.by import By 
service=Service(executable_path=r'C:\Users\user\Desktop\navya\chromedriver.exe')
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://www.flipkart.com/search?q=iphone+13")
driver.maximize_window()
time.sleep(3)



#name of product
names=[]
name=driver.find_elements(By.CLASS_NAME,'_4rR01T')

for i in name:
   names.append(i.text)
print(names)

#current price

#prices=[]
#price=driver.find_elements(By.CLASS_NAME,'1_WHN1')
#for i in price:
#    price.append(i.text)
#print(prices)