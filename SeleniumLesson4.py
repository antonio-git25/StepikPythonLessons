import datetime
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.devtools.v130.browser import cancel_download

# #For firefox
# driver = webdriver.Firefox()
# driver.get('https://www.demoqa.com')
# driver.maximize_window()
# time.sleep(5)
# driver.close()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
#base_url = 'https://demoqa.com/'
base_url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
driver.get(base_url)
driver.maximize_window()

time.sleep(5)
driver.execute_script("window.scrollTo(0, 300)")

checkbox_1 = driver.find_element(By.XPATH, "//input[@value='cb1']")
checkbox_1.click()
time.sleep(2)
checkbox_1.click()
time.sleep(2)
checkbox_1.click()
print("Click checkbox_1")

time.sleep(1)
checkbox_3 = driver.find_element(By.XPATH, "//input[@value='cb3']")


checkbox_2 = driver.find_element(By.XPATH, "//input[@value='cb2']")

if checkbox_1.is_selected(): print("Чек-бокс 1 выбран")
if not checkbox_2.is_selected(): print("Чек-бокс 2 не выбран")
if checkbox_3.is_selected(): print("Чек-бокс 3 выбран")

time.sleep(3)

radio_bt1 = driver.find_element(By.XPATH, "//input[@value='rd1']")
if radio_bt1.is_selected():
    print("rd1 is selected")
else:
    print("rd1 is not selected")
radio_bt1.click()
print("select radio button 1")
if radio_bt1.is_selected(): print("rd1 is selected")


action = ActionChains(driver)
cancel_bt = driver.find_element(By.XPATH, "//input[@value='cancel']")
action.double_click(cancel_bt).perform()

time.sleep(2)

right_click = driver.find_element(By.XPATH, "//input[@value='cancel']")
action.context_click(right_click).perform()



time.sleep(6)
driver.close()

