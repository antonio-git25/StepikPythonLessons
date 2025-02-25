import datetime
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

# #For firefox
# driver = webdriver.Firefox()
# driver.get('https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo')
# driver.maximize_window()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.lambdatest.com/selenium-playground/jquery-dropdown-search-demo'
driver.get(base_url)
driver.maximize_window()

time.sleep(3)

#drop-down1
click_drop1 = driver.find_element(By.XPATH, "//span[@aria-labelledby='select2-country-container']")
click_drop1.click()
time.sleep(2)
click_country = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[3]")
click_country.click()
time.sleep(2)
print(click_drop1.text)

click_drop1.click()
time.sleep(2)
drop1_search_field = driver.find_element(By.XPATH, "(//input[@class='select2-search__field'])[2]")
drop1_search_field.send_keys("India")
time.sleep(1)
drop1_search_field.send_keys(Keys. RETURN)
time.sleep(2)

#drop-down2
click_drop2 = driver.find_element(By.XPATH, "//span[@class='select2-selection select2-selection--multiple']")
click_drop2.click()
time.sleep(2)
click_country2 = driver.find_element(By.XPATH, "(//li[@class='select2-results__option'])[5]")
click_country2.click()
time.sleep(2)
print(click_drop2.text)
time.sleep(2)

#drop-down3 with select
select3 = Select(driver.find_element(By.XPATH, "//select[@name='files']"))
time.sleep(2)
select3.select_by_visible_text('Ruby')



time.sleep(4)
driver.close()