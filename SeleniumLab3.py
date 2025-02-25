import datetime
from random import randint
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.devtools.v85.fetch import continue_request

###Market base stuff
prod1_locator = "//a[@id='item_4_title_link']"  #Sauce Labs Backpack $29.99
prod2_locator = "//a[@id='item_0_title_link']"  #Sauce Labs Bike Light $9.99
prod3_locator = "//a[@id='item_1_title_link']"  #Sauce Labs Bolt T-Shirt $15.99
prod4_locator = "//a[@id='item_5_title_link']"  #Sauce Labs Fleece Jacket $49.99
prod5_locator = "//a[@id='item_2_title_link']"  #Sauce Labs Onesie $7.99
prod6_locator = "//a[@id='item_3_title_link']"  #Test.allTheThings() T-Shirt (Red) $15.99

price1_prodlocator = "(//div[@class='inventory_item_price'])[1]"
price2_prodlocator = "(//div[@class='inventory_item_price'])[2]"
price3_prodlocator = "(//div[@class='inventory_item_price'])[3]"
price4_prodlocator = "(//div[@class='inventory_item_price'])[4]"
price5_prodlocator = "(//div[@class='inventory_item_price'])[5]"
price6_prodlocator = "(//div[@class='inventory_item_price'])[6]"

bye_prod1_bt = "//button[@id='add-to-cart-sauce-labs-backpack']"
bye_prod2_bt = "//button[@id='add-to-cart-sauce-labs-bike-light']"
bye_prod3_bt = "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
bye_prod4_bt = "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"
bye_prod5_bt = "//button[@id='add-to-cart-sauce-labs-onesie']"
bye_prod6_bt = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"


#####user and client info
client_name1 = f"Tomas{randint(1,4)}{randint(5,8)}{randint(1,6)}"
client_name2 = f"Jackson{randint(1,4)}{randint(5,8)}{randint(1,6)}"
client_zip = f"603{randint(1,4)}{randint(5,8)}{randint(1,6)}"
log = 'standard_user'
passw = 'secret_sauce'


###Welcome message
print("Welcome to our Swag Lab market")
print("Choose one of the our product:")
print("Menu:")
print("1 - Sauce Labs Backpack $29.99")
print("2 - Sauce Labs Bike Light $9.99")
print("3 - Sauce Labs Bolt T-Shirt $15.99")
print("4 - Sauce Labs Fleece Jacket $49.99")
print("5 - Sauce Labs Onesie $7.99")
print("6 - Test.allTheThings() T-Shirt (Red) $15.99")

choice = input("please, enter number of product: ")
str1=['1','2','3','4','5','6']
if choice not in str1:
    print("Incorrect input! Please restart app again and enter correct number")
    exit()

print(choice)

#Prepare choisen product
current_prod = ''
current_price = ''
current_bye_bt = ''
if choice == '1':
    current_prod = prod1_locator
    current_price = price1_prodlocator
    current_bye_bt = bye_prod1_bt
elif choice == '2':
    current_prod = prod2_locator
    current_price = price2_prodlocator
    current_bye_bt = bye_prod2_bt
elif choice == '3':
    current_prod = prod3_locator
    current_price = price3_prodlocator
    current_bye_bt = bye_prod3_bt
elif choice == '4':
    current_prod = prod4_locator
    current_price = price4_prodlocator
    current_bye_bt = bye_prod4_bt
elif choice == '5':
    current_prod = prod5_locator
    current_price = price5_prodlocator
    current_bye_bt = bye_prod5_bt
elif choice == '6':
    current_prod = prod6_locator
    current_price = price6_prodlocator
    current_bye_bt = bye_prod6_bt

#Choice information
print("Good choice!")
print("Now, our AI assistent make all steps himself instead of you and bye your product")
print("Please wait...")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument("--headless") #open driver without visual browser
driver = webdriver.Chrome(options=options, service=Service())
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
time.sleep(1)
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

#Find, сhoose and add product to basket
print("Find your stuff in market")
prod1 = driver.find_element(By.XPATH, current_prod)
price1 = driver.find_element(By.XPATH, current_price)
print("Product:", prod1.text, "with price:", price1.text)
add_cart1 = driver.find_element(By.XPATH, current_bye_bt)
add_cart1.click()
print("Product has added into basket")
time.sleep(1)
prod1_etaloname = prod1.text    #find and set as etalon
price1_etalonval = price1.text  #find and set as etalon


#Check basket: index=2 for both products
basket = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
assert basket.text == '1'
print("Basket icon contains one product. index:", basket.text)
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
prod1_basket = driver.find_element(By.XPATH, current_prod)
price1_basket = driver.find_element(By.XPATH, current_price[:-3])
assert prod1_basket.text == prod1_etaloname
assert price1_basket.text == price1_etalonval
print("Product1:", prod1_basket.text, "with price:", price1_basket.text, "is present into basket")

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
prod1_overview = driver.find_element(By.XPATH, current_prod)
price1_overview = driver.find_element(By.XPATH, current_price[:-3])
assert prod1_overview.text == prod1_etaloname
assert price1_overview.text == price1_etalonval
print("Product1:", prod1_overview.text, "with price:", price1_overview.text, "is present into overview order")
item_total = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
item_total_value = item_total.text
assert float(price1_overview.text[1:]) == float(item_total_value[13:])
print(f"{item_total_value}")

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
print("Details:")
print(f"Product: {prod1_etaloname}")
print(f"Price: {price1_etalonval}")
print(f"Total price: {item_total_value[13:]}")


#close driver
time.sleep(4)
driver.close()