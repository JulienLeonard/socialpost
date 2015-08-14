from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import selenium
import win32api, win32con
from win32key import *
import sys

#
# trigger an OS click event
#
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#
# check that the pin "title" exits in pinterest
#
def checkpostpinterest(userid,pinboard,title):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://www.pinterest.com/" + userid + "/" + pinboard + "/")
    pins = driver.find_elements(By.XPATH, '//a[@title="' + title + '"]')
    if len(pins) > 0:
        pin = pins[0]
        pinid = pin.get_attribute("href")
        result =  pinid
    else:
        result = ""

    if len(result) == 0:
        for elem in driver.find_elemts(By.CLASS, "pinDescription"):
            if title in elem.text:
                result = "OK"
                break

    driver.close()
    return result

#
# post an image as a pin on pinterest from a wordpress post
#
def pinterest_post(email_adress,password,pinboard,title,wordpress_post_url):

    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)

    # open wordpress post url
    driver.get(wordpress_post_url)

    # move the cursor to the share button, to display the sub sharing buttons
    sharedaddy = driver.find_element_by_class_name("sharing-anchor")
    actions1 = ActionChains(driver)
    actions1.move_to_element(sharedaddy).click().perform();
    time.sleep(2)
    elem = driver.find_element_by_class_name("share-pinterest")
    actions2 = ActionChains(driver)
    actions2.move_to_element(elem).perform();
    time.sleep(2)

    # use tab to select the pinterest button and trigger
    press('tab')
    press('tab')
    press('tab')
    press('enter')

    # wait for the pin choice window to open, then click
    time.sleep(10)    
    click(150,600)
    
    # wait for the login window to open, then log
    time.sleep(30)
    typer(email_adress)
    press('tab')
    typer(password)
    press('enter')

    # wait for the tableau window to open, then choose tableau
    time.sleep(30)
    typer(pinboard)
    press('enter')

    time.sleep(20)

    driver.close()

