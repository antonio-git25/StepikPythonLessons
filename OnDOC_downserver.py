import datetime
from random import randint
import random
import string
import time #for time sleep option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #for chrome webdriver fix problem with closing
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument("--headless") #open driver without visual browser
# driver1 = webdriver.Chrome(options=options, service=Service())
#base_url = 'https://www.saucedemo.com/'
#driver.get(base_url)
#driver1.maximize_window()

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


def ONDoc_contactform():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")  # open driver without visual browser
    driver1 = webdriver.Chrome(options=options, service=Service())
    driver1.get('https://ondoc.me/contacts/')
    driver1.maximize_window()
    time.sleep(2)

    name = driver1.find_element(By.XPATH, "//input[@type='text']")
    email = driver1.find_element(By.XPATH, "//input[@type='email']")
    cell = driver1.find_element(By.XPATH, "//input[@type='tel']")
    text = driver1.find_element(By.XPATH, "//textarea[@class='large-contact-form__Textarea-sc-16odb4k-4 eTffxw']")
    send_bt = driver1.find_element(By.XPATH, "//button[@type='submit']")

    #Data generation
    name_gen = f"performance_data_test{randint(1,4)}{randint(10,90)}{randint(50,80)}"
    email_gen = f"blackhack{randint(1,9)}{randint(10,99)}@gmail.com"
    cell_gen = f"+7{random.choice(['906','902','908','960','910','950'])}{randint(340,820)}{randint(10,90)}{randint(10,90)}"
    text_gen = randomword(50)

    #Data send
    name.send_keys(name_gen)
    email.send_keys(email_gen)
    cell.send_keys(cell_gen)
    itr2 = 1
    while itr2 < 20:
        text.send_keys(text_gen)
        itr2 += 1
    send_bt.click()

    time.sleep(1)
    #Check sending
    send_bt_value = send_bt.text
    #Заявка отправлена
    print(f"send: {send_bt_value} {name_gen} {email_gen} {cell_gen}")

    time.sleep(2)
    driver1.close()



def ONDoc_supportform():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #options.add_argument("--headless")  # open driver without visual browser
    driver1 = webdriver.Chrome(options=options, service=Service())
    driver1.get('https://lk.ondoc.me/issue/create')
    driver1.maximize_window()
    time.sleep(2)

    name1 = driver1.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section/form/section[1]/div/div[2]/input")
    name2 = driver1.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section/form/section[1]/div/div[1]/input")
    email = driver1.find_element(By.XPATH, "//input[@type='email']")
    cell = driver1.find_element(By.XPATH, "//input[@type='tel']")
    topic = driver1.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section/form/section[2]/div[1]/div[1]/input")
    text = driver1.find_element(By.XPATH, "//*[@id='root']/div[2]/div/section/form/section[2]/div[2]/div[1]/div[2]/div")
    send_bt = driver1.find_element(By.XPATH, "//button[@type='submit']")

    #Data generation
    name1_gen = f"gpt{randint(1,4)}{randint(10,90)}{randint(50,80)}"
    name2_gen = f"gpt{randint(1, 4)}{randint(10, 90)}{randint(50, 80)}"
    email_gen = f"blackhack{randint(1,9)}{randint(10,99)}@gmail.com"
    cell_gen = f"{random.choice(['906','902','908','960','910','950'])}{randint(340,820)}{randint(10,90)}{randint(10,90)}"
    topic_gen = f"performance_data_test{randint(1, 4)}{randint(10, 90)}{randint(50, 80)}"
    text_gen = randomword(100)

    #Data send
    name1.send_keys(name1_gen)
    name2.send_keys(name2_gen)
    email.send_keys(email_gen)
    cell.send_keys(cell_gen)
    topic.send_keys(topic_gen)
    itr2 = 1
    while itr2 < 20:
        text.send_keys(text_gen)
        itr2 += 1
    send_bt.click()
    time.sleep(3)
    order = driver1.find_element(By.XPATH, "//*[@id='root']/div[2]/section/section/p/div")
    print(order.text)
    success_head = driver1.find_element(By.XPATH, "//h2[@class='SectionTitle-sc-da6ear-0 krrZTg']")
    if success_head.text == 'Ваше сообщение отправлено': print("order success")

    time.sleep(2)
    driver1.close()


def ONDoc_patient_registry():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    #options.add_argument("--headless")  # open driver without visual browser
    driver1 = webdriver.Chrome(options=options, service=Service())
    driver1.get('https://lk.ondoc.me/login')
    driver1.maximize_window()
    time.sleep(2)

    #click email switch
    #email_bt = driver1.find_element(By.XPATH, "//label[@for=':r1:']")
    #email_bt.click()
    phone = driver1.find_element(By.XPATH, "//input[@type='tel']")
    phone_gen = f"{random.choice(['906','902','908','960','910','950'])}{randint(340,820)}{randint(10,90)}{randint(10,90)}"
    phone.send_keys(phone_gen)
    submit1 = driver1.find_element(By.XPATH, "//button[@type='submit']")
    submit1.click()
    time.sleep(3)
    one_time_field = driver1.find_element(By.XPATH, "//input[@autocomplete='one-time-code']")
    temp_pass = f"{randint(340,820)}{randint(40,80)}"
    one_time_field.send_keys(temp_pass)
    submit2 = driver1.find_element(By.XPATH, "//button[@type='submit']")
    submit2.click()



#ONDoc_patient_registry()

#Uncomment and execute any function
count=1
while count < 50:
    print(f"count: {count}")
    ONDoc_contactform()
    count += 1

print("call of ONDoc_contactform() is completed! count:", str(count))


