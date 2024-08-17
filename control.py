from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def testSelNetAccess():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/')
    print('network access success')

def openApp(link):
    options = Options()
    #options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/')
    print('network access success')
    driver.get(link)
    print('app reached')
    time.sleep(3)

    text_box = driver.find_element(by=By.CLASS_NAME, value='fn-input__text-field.ids-input.ids-input--text.ids-input--clear.js-has-input-clear.js-login-toggle-active-input-user')
    text_box.send_keys('test')
    print('sent test id')
    time.sleep(20)
openApp('https://basic-trial-sac-eu10.cfapps.eu10.hana.ondemand.com/sap/fpa/ui/app.html#/')
