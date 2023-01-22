from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager
import time
import os

###########################################################

# enter the link to the website you want to automate login.
website_link = "https://gateway.iitk.ac.in:1003/login?37a0dda83f485e25"
# enter your login username
username = "atanusroy22"
# enter your login password
password = "v@KfTJ8dTLTaNBy"

###########################################################

# enter the element for username input field
element_for_username = "username"
# enter the element for password input field
element_for_password = "password"
# enter the element for submit button
element_for_submit = "Continue"

###########################################################
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
options.headless = True
browser = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)
# browser = webdriver.Safari()  # for macOS users[for others use chrome vis chromedriver]
# browser = webdriver.Chrome()	#uncomment this line,for chrome users
browser.get(website_link)
time.sleep(3)

try:
    username_element = browser.find_element(by=By.NAME, value=element_for_username)
    username_element.send_keys(username)
    password_element = browser.find_element(by=By.NAME, value=element_for_password)
    password_element.send_keys(password)
    signInButton = browser.find_element(by=By.XPATH, value='/html/body/div[1]/form/div[3]/button')
    signInButton.click()

#### to quit the browser uncomment the following lines ####
# time.sleep(3)
# browser.quit()
# time.sleep(1)
# browserExe = "Safari"
# os.system("pkill "+browserExe)
except Exception:
    #### This exception occurs if the element are not found in the webpage.
    print("Some error occured :(")

#### to quit the browser uncomment the following lines ####
# browser.quit()
# browserExe = "Safari"
# os.system("pkill "+browserExe)
