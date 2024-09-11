from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
import time

options = Options()
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

def testSelNetAccess():
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # #driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/')
    print('network access success')

def openApp(link):
    # options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    #driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.com/')
    print('network access success')
    driver.get(link)
    print('app reached')
    time.sleep(3)

    u_id = driver.find_element(by=By.CLASS_NAME, value='fn-input__text-field.ids-input.ids-input--text.ids-input--clear.js-has-input-clear.js-login-toggle-active-input-user')
    u_id.send_keys('GE109894') #GE109894
    print('sent test id')
    time.sleep(5)

    pw = driver.find_element(by=By.CLASS_NAME, value='fn-input__text-field.ids-input.ids-input--text.ids-input--reveal.js-login-toggle-active-input-password')
    pw.send_keys('ObpO17MO1c1!') #ObpO17MO1c1! 
    print('sent pw')
    time.sleep(5)
    pw.submit()
    time.sleep(15)

def select_story():
    stories = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/aside/div[2]/div/div[2]/ul/li[1]')
    print('found stories')
    ActionChains(driver)\
        .click(stories)\
        .perform()
    print('selected stories')
    time.sleep(5)

def create_story():
    responsive = driver.find_element(by=By.CLASS_NAME, value='sapMTileCntContent')
    print('found responsive story')
    ActionChains(driver)\
        .click(responsive)\
        .perform()
    time.sleep(5)
    confirmation = driver.find_element(by=By.CLASS_NAME, value='sapMBtnBase.sapMBtn.sapMBtnInverted.sapEpmUiDialogOkButton.sapEpmUiDialogButton.sapMDialogBeginButton.sapMBarChild')
    print('selected story')
    ActionChains(driver)\
        .click(confirmation)\
        .perform()
    print('reached buildable story')
    time.sleep(5)

def upload_new_data():
    driver.maximize_window()
    add_data = driver.find_element(by=By.CLASS_NAME, value='sapUiIcon.sapUiIconMirrorInRTL')
    print('found upload tool')
    ActionChains(driver)\
        .click(add_data)\
        .perform()
    time.sleep(5)
    upload = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[1]/div[2]/div[1]/div/div[3]/div/div/div/div[2]/div/section/div/div/div[1]/div/div/div[1]/div/div[2]/div/div/div/div[5]/div[2]/div[1]/button/div/div/span[1]')
    ActionChains(driver)\
        .click(upload)\
        .perform()
    print('selected to upload data from file')
    time.sleep(5)
    select_source = driver.find_element(by=By.CLASS_NAME, value='add-new-data-in-story-dialog')
    ActionChains(driver)\
        .click(select_source)\
        .perform()
    print('selecting source for upload...')
    time.sleep(5)
    still_selecting = driver.find_element(by=By.ID, value='__section38-dm-file-uploader-fu_button')
    ActionChains(driver)\
        .click(select_source)\
        .perform()
    print('...continuing to select source for upload...')
    time.sleep(5)

openApp('https://basic-trial-sac-eu10.cfapps.eu10.hana.ondemand.com/sap/fpa/ui/app.html#/')
select_story()
create_story()
upload_new_data()