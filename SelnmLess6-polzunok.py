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
base_url = 'https://html5css.ru/howto/howto_js_rangeslider.php'
driver.get(base_url)
time.sleep(5)
driver.maximize_window()
time.sleep(4)


print("Square polzunok")
action = ActionChains(driver)
square = driver.find_element(By.XPATH, "//input[@id='id2']")
action.click_and_hold(square).move_by_offset(120,0).release().perform()
time.sleep(1)
action.click_and_hold(square).move_by_offset(240,0).release().perform()
time.sleep(1)
action.click_and_hold(square).move_by_offset(360,0).release().perform()
time.sleep(1)
action.click_and_hold(square).move_by_offset(0,0).release().perform()
time.sleep(1)
action.click_and_hold(square).move_by_offset(-120,0).release().perform()
time.sleep(1)
action.click_and_hold(square).move_by_offset(-240,0).release().perform()
time.sleep(1)
action.click_and_hold(square).move_by_offset(-360,0).release().perform()

time.sleep(3)

print("Square circle")
action = ActionChains(driver)
circle = driver.find_element(By.XPATH, "//input[@id='id1']")
action.click_and_hold(circle).move_by_offset(150,0).release().perform()
time.sleep(1)
action.click_and_hold(circle).move_by_offset(300,0).release().perform()
time.sleep(1)
action.click_and_hold(circle).move_by_offset(850,0).release().perform()
time.sleep(1)
action.click_and_hold(circle).move_by_offset(-150,0).release().perform()
time.sleep(1)
action.click_and_hold(circle).move_by_offset(-300,0).release().perform()
time.sleep(1)
action.click_and_hold(circle).move_by_offset(-450,0).release().perform()
time.sleep(1)






time.sleep(6)
driver.close()