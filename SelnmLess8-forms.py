import datetime
import os
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
base_url = 'https://www.lambdatest.com/selenium-playground/simple-form-demo'
driver.get(base_url)
time.sleep(10)
driver.maximize_window()
time.sleep(5)

#First part
text1 = 'Fuck you, asshole!!!'
text2 = 'Fuck you, shit!!!'
text3 = 'Fuck you, bitch!!!'
message = driver.find_element(By.XPATH, "//input[@id='user-message']")
message.send_keys(text1)
time.sleep(1)
click_bt1 = driver.find_element(By.XPATH, "//button[@id='showInput']")
click_bt1.click()
time.sleep(1)
check_msg = driver.find_element(By.XPATH, "//p[@id='message']")
assert check_msg.text == text1
print(check_msg.text)

message.clear()
time.sleep(1)
message.send_keys(text2)
time.sleep(1)
click_bt1.click()
time.sleep(1)
assert check_msg.text == text2
print(check_msg.text)
time.sleep(1)

message.clear()
time.sleep(1)
message.send_keys(text3)
time.sleep(1)
click_bt1.click()
time.sleep(1)
assert check_msg.text == text3
print(check_msg.text)
time.sleep(1)



#Second part
num_1 = 200
num_2 = 456
input_1 = driver.find_element(By.XPATH, "//input[@id='sum1']")
input_2 = driver.find_element(By.XPATH, "//input[@id='sum2']")
click_bt2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Get Sum')]")
input_1.send_keys(str(num_1))
time.sleep(1)
input_2.send_keys(str(num_2))
time.sleep(1)
click_bt2.click()
time.sleep(2)
check_sum = driver.find_element(By.XPATH, "//p[@id='addmessage']")
assert check_sum.text == str(num_1 + num_2)
print(check_sum.text)

time.sleep(4)
driver.close()


#Upload file part
####################################
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())

base_url = 'https://www.lambdatest.com/selenium-playground/upload-file-demo'
driver.get(base_url)
time.sleep(8)
driver.maximize_window()
time.sleep(4)

path_file = "C:\\Users\\Antonio\\PycharmProjects\\StepikPythonLessons\\doc\\screen2025.02.14.13.39.29.png"
upload_bt = driver.find_element(By.XPATH, "//input[@id='file']")
upload_bt.send_keys(path_file)
time.sleep(2)

accept_file = driver.find_element(By.XPATH, "//input[@id='file']")
accept_msg = driver.find_element(By.XPATH, "//div[@id='error']")
print("File path:", accept_file.text)
assert accept_msg.text == 'File Successfully Uploaded'
print(accept_msg.text)
print("File Successfully Uploaded")

time.sleep(4)
driver.close()


#Download file part
####################################
options = webdriver.ChromeOptions()
#{
download_path = path_file = "C:\\Users\\Antonio\\PycharmProjects\\StepikPythonLessons\\doc\\"
prefs = {'download.default_directory' : download_path}
options.add_experimental_option('prefs', prefs)
#}
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service())

base_url = 'https://www.lambdatest.com/selenium-playground/download-file-demo'
driver.get(base_url)
time.sleep(8)
driver.maximize_window()
time.sleep(4)

down_bt = driver.find_element(By.XPATH, "//button[contains(text(),'Download File')]")
down_bt.click()
print("Download button")
time.sleep(2)

if os.listdir(download_path): print("directory is not empty")
#print(os.listdir(download_path))
for str in os.listdir(download_path):
    print(str)

file_name = "LambdaTest.pdf"
file_path = download_path + file_name
assert os.access(file_path, os.F_OK) == True
print("downloaded file is present in directory")


time.sleep(4)
driver.close()