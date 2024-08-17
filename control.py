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

    u_id = driver.find_element(by=By.CLASS_NAME, value='fn-input__text-field.ids-input.ids-input--text.ids-input--clear.js-has-input-clear.js-login-toggle-active-input-user')
    u_id.send_keys('test')
    print('sent test id')
    time.sleep(5)

    pw = driver.find_element(by=By.CLASS_NAME, value='fn-input__text-field.ids-input.ids-input--text.ids-input--reveal.js-login-toggle-active-input-password')
    pw.send_keys('test')
    print('sent pw')
    time.sleep(5)
    pw.submit()
    time.sleep(15)
openApp('https://basic-trial-sac-eu10.cfapps.eu10.hana.ondemand.com/sap/fpa/ui/app.html#/')
