import datetime
from random import randint
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

client_name1 = f"Tomas{randint(1,4)}{randint(5,8)}{randint(1,6)}"
client_name2 = f"Jackson{randint(1,4)}{randint(5,8)}{randint(1,6)}"
client_zip = f"603{randint(1,4)}{randint(5,8)}{randint(1,6)}"
log = 'standard_user'
passw = 'secret_sauce'
prod1_locator = "//a[@id='item_4_title_link']"
prod2_locator = "//a[@id='item_0_title_link']"
price1_locator = "(//div[@class='inventory_item_price'])[1]"
price2_locator = "(//div[@class='inventory_item_price'])[2]"
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
password = driver.find_element(By.XPATH, "//input[@id='password']")
button_login = driver.find_element(By.XPATH, "//input[@name='login-button']")


#Login in market
print("Market authentification")
username.send_keys(log)
print("Input login")
time.sleep(1)
password.send_keys(passw)
print("Input password")
time.sleep(1)
button_login.click()
print("Click login")
time.sleep(3)


#Check autorization
text_products = driver.find_element(By.XPATH, "//span[@class='title']") #//span[@class='title']
value_text_products = text_products.text
assert value_text_products == 'Products'

url1 = "https://www.saucedemo.com/inventory.html" #inventory page after avtorization
get_url1 = driver.current_url
assert url1 == get_url1
print("Autorization complete successfully!")
time.sleep(1)


#Find, сhoose and add first product to basket
print("Find first stuff in market")
prod1 = driver.find_element(By.XPATH, prod1_locator)
price1 = driver.find_element(By.XPATH, price1_locator)
print("Product1:", prod1.text, "with price:", price1.text)
add_cart1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
add_cart1.click()
print("Product1 has added into basket")
time.sleep(1)
prod1_etaloname = prod1.text    #find and set as etalon
price1_etalonval = price1.text  #find and set as etalon


#Find, сhoose and add second product to basket
print("Find second stuff in market")
prod2 = driver.find_element(By.XPATH, prod2_locator)
price2 = driver.find_element(By.XPATH, price2_locator)
print("Product1:", prod2.text, "with price:", price2.text)
#(//button[contains(text(), 'Add to cart')])[1]
add_cart2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
add_cart2.click()
print("Product2 has added into basket")
time.sleep(1)
prod2_etaloname = prod2.text    #find and set as etalon
price2_etalonval = price2.text  #find and set as etalon


#Check basket: index=2 for both products
basket = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
assert basket.text == '2'
print("Basket icon contains both products. index:", basket.text)
time.sleep(1)
basket.click()
time.sleep(3)


#Check basket page current location
text_basket = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_basket = text_basket.text
assert value_text_basket == 'Your Cart'
url2 = "https://www.saucedemo.com/cart.html" #cart page
get_url2 = driver.current_url
assert url2 == get_url2
print("Moved to basket successfully!")
time.sleep(1)

#Check that basket contains our products with prices
prod1_basket = driver.find_element(By.XPATH, prod1_locator)
price1_basket = driver.find_element(By.XPATH, price1_locator)
prod2_basket = driver.find_element(By.XPATH, prod2_locator)
price2_basket = driver.find_element(By.XPATH, price2_locator)
assert prod1_basket.text == prod1_etaloname
assert prod2_basket.text == prod2_etaloname
assert price1_basket.text == price1_etalonval
assert price2_basket.text == price2_etalonval
print("Product1:", prod1_basket.text, "with price:", price1_basket.text, "is present into basket")
print("Product2:", prod2_basket.text, "with price:", price2_basket.text, "is present into basket")

#Checkout
checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
checkout.click()
print("Checkout order")
time.sleep(3)


#Checkout information page location
text_checkout = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_checkout = text_checkout.text
assert value_text_checkout == 'Checkout: Your Information'
url3 = "https://www.saucedemo.com/checkout-step-one.html" #Checkout: Your Information page
get_url3 = driver.current_url
assert url3 == get_url3
print("Checkout: Your Information page location is successfully!")
time.sleep(1)

#Client personal data input
name_f = driver.find_element(By.XPATH, "//input[@id='first-name']")
name_l = driver.find_element(By.XPATH, "//input[@id='last-name']")
zipcod = driver.find_element(By.XPATH, "//input[@id='postal-code']")
continue_bt = driver.find_element(By.XPATH, "//input[@id='continue']")

name_f.send_keys(client_name1)
time.sleep(0.5)
name_l.send_keys(client_name2)
time.sleep(0.5)
zipcod.send_keys(client_zip)
time.sleep(0.5)
continue_bt.click()
print("Continue order...")
time.sleep(3)


#Checkout: Overview page location
text_checkout2 = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_checkout2 = text_checkout2.text
assert value_text_checkout2 == 'Checkout: Overview'
url4 = "https://www.saucedemo.com/checkout-step-two.html" #Checkout: Overview page location
get_url4 = driver.current_url
assert url4 == get_url4
print("Checkout: Overview page location is successfully!")
time.sleep(1)

#Check products, prices and item total price
prod1_overview = driver.find_element(By.XPATH, prod1_locator)
price1_overview = driver.find_element(By.XPATH, price1_locator)
prod2_overview = driver.find_element(By.XPATH, prod2_locator)
price2_overview = driver.find_element(By.XPATH, price2_locator)
assert prod1_overview.text == prod1_etaloname
assert prod2_overview.text == prod2_etaloname
assert price1_overview.text == price1_etalonval
assert price2_overview.text == price2_etalonval
print("Product1:", prod1_overview.text, "with price:", price1_overview.text, "is present into overview order")
print("Product2:", prod2_overview.text, "with price:", price2_overview.text, "is present into overview order")
item_total = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
item_total_value = item_total.text
assert float(price1_overview.text[1:]) + float(price2_overview.text[1:]) == float(item_total_value[13:])
print(f"{item_total_value} ({price1_etalonval} + {price2_etalonval})")

#Finish
finish = driver.find_element(By.XPATH, "//button[@id='finish']")
finish.click()
print("Order is finished!")
time.sleep(3)


#Check order completion
text_checkout3 = driver.find_element(By.XPATH, "//span[@class='title']")
value_text_checkout3 = text_checkout3.text
url5 = "https://www.saucedemo.com/checkout-complete.html" #Checkout: Complete! page location
get_url5 = driver.current_url
conf_msg = driver.find_element(By.XPATH, "//h2[@class='complete-header']")
conf_msg_value = conf_msg.text
assert value_text_checkout3 == 'Checkout: Complete!'
assert url5 == get_url5
assert conf_msg_value == 'Thank you for your order!'

print("Thank you for your order!")


#close driver
time.sleep(4)
driver.close()