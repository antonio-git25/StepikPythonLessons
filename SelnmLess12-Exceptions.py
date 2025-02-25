import datetime
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.devtools.v130.browser import cancel_download


##Working with alert msg
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
time.sleep(5)
driver.maximize_window()
time.sleep(3)




time.sleep(3)
driver.close()

