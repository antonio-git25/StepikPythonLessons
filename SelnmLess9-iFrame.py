import datetime
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.devtools.v130.browser import cancel_download


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.lambdatest.com/selenium-playground/iframe-demo/'
driver.get(base_url)
time.sleep(8)
driver.maximize_window()
time.sleep(4)


###
iframe = driver.find_element(By.XPATH, "//iframe[@id='iFrame1']") #//iframe[@id='iFrame1']
driver.switch_to.frame(iframe)

frame_filed = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]")
val1 = frame_filed.text
print(val1)
frame_filed.send_keys(Keys.CONTROL + 'a')
edition_panel = driver.find_element(By.XPATH, "//button[@title='Bold']")
edition_panel.click()
print("click aditional panel bolt")

new_ff = driver.find_element(By.XPATH, "//div[@id='__next']/div/div[2]/b")
value_new_ff = new_ff.text
print(value_new_ff)

assert val1 == value_new_ff
print("edit is successful")








time.sleep(3)
driver.close()




