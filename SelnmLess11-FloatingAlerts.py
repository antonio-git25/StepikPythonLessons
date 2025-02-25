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
base_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(base_url)
time.sleep(5)
driver.maximize_window()
time.sleep(3)


##Click for JS Alert
js_alert_bt = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
js_alert_bt.click()
print("click alert button")
print(driver.switch_to.alert.text)
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)
result = driver.find_element(By.XPATH, "//p[@id='result']")
assert result.text == 'You successfully clicked an alert'
print('You successfully clicked an alert')
print('\n')



##Click for JS Confirm
js_cnfrm_bt = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
js_cnfrm_bt.click()
print("click for js confirm button")
print(driver.switch_to.alert.text)
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(2)
result = driver.find_element(By.XPATH, "//p[@id='result']")
assert result.text == 'You clicked: Ok'
print('You clicked: Ok')
print('\n')

js_cnfrm_bt.click()
print("click for js confirm button")
print(driver.switch_to.alert.text)
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(2)
result = driver.find_element(By.XPATH, "//p[@id='result']")
assert result.text == 'You clicked: Cancel'
print('You clicked: Cancel')
print('\n')


##Click for JS Promt
js_promt_bt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
js_promt_bt.click()
print("click for js promt button")
print(driver.switch_to.alert.text)
time.sleep(3)
driver.switch_to.alert.dismiss()
time.sleep(2)
result = driver.find_element(By.XPATH, "//p[@id='result']")
assert result.text == 'You entered: null'
print('You entered: null')
print('\n')

js_promt_bt.click()
print("click for js promt button")
print(driver.switch_to.alert.text)
time.sleep(3)
input_line = 'fuck you'
driver.switch_to.alert.send_keys(input_line)
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(2)
result = driver.find_element(By.XPATH, "//p[@id='result']")
assert result.text == f"You entered: {input_line}"
print(f"You entered: {input_line}")
print('\n')


time.sleep(3)
driver.close()

