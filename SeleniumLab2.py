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
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
time.sleep(10)
driver.maximize_window()
time.sleep(5)


feature_day = 10
feature_date = datetime.datetime.today() + datetime.timedelta(days=feature_day)
print(f"today: {datetime.datetime.today()}")
print(f"after 10 days: {feature_date.strftime("%m.%d.%Y")}")

feature_date_input = f"{feature_date.strftime("%m")}/{feature_date.strftime("%d")}/{feature_date.strftime("%Y")}"
print("Feature date: ", feature_date_input)

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
new_date.send_keys(Keys.BACKSPACE)
time.sleep(2)
new_date.send_keys(feature_date_input)  #format: MM\DD\YY
time.sleep(2)
new_date.send_keys(Keys.RETURN)
print("Date is applied!")


time.sleep(6)
driver.close()