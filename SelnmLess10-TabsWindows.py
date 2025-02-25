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
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
time.sleep(8)
driver.maximize_window()
time.sleep(4)


##Switching between tabs
tab_bt = driver.find_element(By.XPATH, "//button[@id='tabButton']")
tab_bt.click()
print("click tab button")
time.sleep(3)
print(driver.current_url)

header_1 = driver.find_element(By.XPATH, "//h1[@class='text-center']")
print(header_1.text)

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
print(driver.current_url)
header_2 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(header_2.text)

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
print(driver.current_url)

time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.close()




##Switching between windows
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
time.sleep(8)
driver.maximize_window()
time.sleep(4)


win_bt = driver.find_element(By.XPATH, "//button[@id='windowButton']")
win_bt.click()
print("click new win button")
time.sleep(3)
print(driver.current_url)

#header_3 = driver.find_element(By.XPATH, "//div[@class='main-header']")
header_3 = driver.find_element(By.XPATH, "//h1[@class='text-center']")
print(header_3.text)
window_1 = driver.window_handles[0]
window_2 = driver.window_handles[1]

driver.switch_to.window(window_2)
time.sleep(2)

header_4 = driver.find_element(By.XPATH, "//h1[@id='sampleHeading']")
print(header_4.text)

driver.switch_to.window(window_1)
time.sleep(2)
print(driver.current_url)
print(header_3.text)


time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.close()



##Switching to info wondow
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://demoqa.com/browser-windows'
driver.get(base_url)
time.sleep(8)
driver.maximize_window()
time.sleep(4)


win_msg_bt = driver.find_element(By.XPATH, "//button[@id='messageWindowButton']")
win_msg_bt.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])

#print(driver.switch_to.alert.text)

time.sleep(3)
driver.close()

