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
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
time.sleep(10)
driver.maximize_window()
time.sleep(5)


# new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
# #new_date.clear()
# new_date.send_keys(Keys.CONTROL + 'a')
# time.sleep(1)
# new_date.send_keys(Keys.BACKSPACE)
# time.sleep(5)
# new_date.send_keys("12/12/2026")
# time.sleep(5)
# new_date.send_keys(Keys.RETURN)


new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.click()
time.sleep(4)
date_20 = driver.find_element(By.XPATH, "//div[@aria-label='Choose Thursday, February 20th, 2025']")
date_20.click()

time.sleep(3)

new_date.click()
time.sleep(4)
date_today = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")  #//div[contains(@class, 'react-datepicker__day--today')]
date_today.click()


#Test task#3
now_date = datetime.datetime.now().strftime("%m.%d.%Y")
now_date_day = datetime.datetime.now().strftime("%d")
now_date_month = datetime.datetime.now().strftime("%m")
now_date_year = datetime.datetime.now().strftime("%Y")
print("Current date: ", now_date)
print("Current day: ", now_date_day)
print("Current month: ", now_date_month)
print("Current year: ", now_date_year)
feature_day = '10'
feature_date_input = f"{now_date_month}/{int(now_date_day) + int(feature_day)}/{now_date_year}"
print("Feature date: ", feature_date_input)

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
#new_date.clear()
new_date.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
new_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
new_date.send_keys(feature_date_input)  #format: MM\DD\YY
time.sleep(2)
new_date.send_keys(Keys.RETURN)





time.sleep(6)
driver.close()