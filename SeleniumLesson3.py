import datetime
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select    # импортирование класса Select, для работы с дроп-даунами


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

log = 'standard_user'
passw = 'secret_sauce'

username = driver.find_element(By.XPATH, "//input[@id='user-name']")
password = driver.find_element(By.XPATH, "//input[@id='password']")
button_login = driver.find_element(By.XPATH, "//input[@name='login-button']")
username.send_keys(log)
time.sleep(2)
username.send_keys(Keys.CONTROL + 'a')
time.sleep(2)
print("Input login")
time.sleep(1)
password.send_keys(passw)
print("Input password = ", passw)
time.sleep(2)

username.clear()
time.sleep(2)
password.clear()
time.sleep(2)

username.send_keys(log)
time.sleep(1)
password.clear()
time.sleep(1)
password.send_keys(passw)
print("Input password 2nd time = ", passw)
time.sleep(1)

button_login.click()
print("Click login")
time.sleep(4)

text_products = driver.find_element(By.XPATH, "//span[@class='title']") #//span[@class='title']
value_text_products = text_products.text
print(value_text_products)

assert value_text_products == 'Products'
print("GOOD")
now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
name_screen = 'screen' + now_date + '.png'
#driver.save_screenshot(f"\\doc\\{name_screen}")
driver.save_screenshot('C:\\Users\\Antonio\\PycharmProjects\\StepikPythonLessons\\doc\\' + name_screen)


url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)

assert url == get_url
print("Good URL")
time.sleep(1)


filter = driver.find_element(By.XPATH, "//select[@data-test='product-sort-container']")
filter.click()
print("Click filter")
time.sleep(3)
filter.send_keys(Keys.DOWN)
time.sleep(3)
filter.send_keys(Keys.RETURN)

#Make drop-down manipulations
select = Select(driver.find_element(By.XPATH, "//select[@class='product_sort_container']"))
time.sleep(2)
#select.select_by_visible_text('Price (low to high)')
select.select_by_value('hilo')


#make scrolling of page with stuff
time.sleep(1)
driver.execute_script("window.scrollTo(0, 500)")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 400)")
time.sleep(2)
driver.execute_script("window.scrollTo(0, -300)")
time.sleep(2)


action = ActionChains(driver)
black_bag = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
action.move_to_element(black_bag).perform()
time.sleep(2)
now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
name_screen = 'screen' + now_date + '.png'
driver.save_screenshot('C:\\Users\\Antonio\\PycharmProjects\\StepikPythonLessons\\doc\\' + name_screen)


#Logout step
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
out = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
menu.click()
time.sleep(2)
out.click()
time.sleep(3)

#back button
driver.back()
time.sleep(3)
driver.forward()

time.sleep(4)
driver.close()