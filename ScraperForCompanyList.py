from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup

import os
import openai

from dotenv import load_dotenv
from idlelib.query import Goto


#DRIVER_PATH = "C:\Program Files\Google\ChromeDriver\chromedriver.exe"

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, options=options)



#Variabeln:
# website = "https://clusterix.io/companies"
website = "https://www.agritechnica.com/en/exhibitors-products#/search/f=h-entity_orga;v_sg=0;v_fg=0;v_fpa=FUTURE"


driver.get(website)
sleep(10)

button = driver.find_element(By.XPATH,'//*[@id="onlineGuide"]/div/div[4]/div[2]/div[2]/div[4]/div[1]')
for x in range(113)
	button.click()
	sleep(2)

stand = driver.find_elements(By.CLASS_NAME,'gwt-Label.EWP5KKC-w-a')
name = driver.find_elements(By.CLASS_NAME,'gwt-Label.EWP5KKC-w-Q')
land = driver.find_elements(By.CLASS_NAME,'gwt-Label.EWP5KKC-w-m')



for id, x in enumerate(name):
	if 'Germany' not in str(land[id].text)
		print(x.text + ', ' + str(stand[id].text))
	else:
		continue
	
	




'''
for x in range(24):
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	sleep(2)

firmen = driver.find_elements(By.CLASS_NAME,"searchresult-box__head")
stand = driver.find_elements(By.CLASS_NAME,"link-fix--text")

for id, x in enumerate(firmen):
	html = x.get_attribute('innerHTML')
	soup = BeautifulSoup(html, 'html.parser')
	div_text_1 = x.text
	#div_text_1 = soup.find_all('div', {'class' : 'nfprofile-company'})
	#div_text_2 = soup.find_all('div', {'class' : 'nfprofile-location'})
                
	#print(div_text_1[0].text + ', ' + div_text_2[0].text + ', ')
	print(div_text_1 + "," + stand[id].text)
'''


	
