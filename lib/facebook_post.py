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
from utils import *

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
    # click(location['x'] + 25,1024-location['y'] + 45)
    # click(650,130)

def checkpostfacebook(email,password,profileID,siteID,title):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
	
    # first login
    driver.get("https://www.facebook.com/login")
    click(200,200)

    press('tab')
    typer(email)
    press('tab')
    typer(password)
    press('enter')

    time.sleep(2)

    # then open profile
    driver.get("http://www.facebook.com/profile.php?id=" + profileID)
    pins = driver.find_elements(By.XPATH, '//a[text()="' + title + ' | ' + siteID + '"]')
    if len(pins) > 0:
        result =  "OK"
    else:
        result = ""
    puts("result",result)
    driver.close()
    return result

def facebook_post(email,password,profileID,siteID,title,url):

    log       = open("postfacebook_logs.txt", 'w')
    log.truncate()

    log.write("START: post " + title + " \n")
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)

    # open wordpress post url
    driver.get(url)

    # move the cursor to the share button, to display the sub sharing buttons
    sharedaddy = driver.find_element_by_class_name("sharing-anchor")
    actions1 = ActionChains(driver)
    actions1.move_to_element(sharedaddy).click().perform();
    time.sleep(2)
    elem = driver.find_element_by_class_name("share-facebook")
    actions2 = ActionChains(driver)
    actions2.move_to_element(elem).perform();
    time.sleep(2)

    # use tab to select the facebook button and trigger
    press('tab')
    press('tab')
    press('enter')

    # wait for the login window to open, then log
    time.sleep(5)
    press('tab')
    time.sleep(3)
    typer(email)
    press('tab')
    typer(password)
    press('enter')

    # wait for the post window to open the press post button
    time.sleep(5)
    for i in range(7):
        press('tab')
    press('enter')

    time.sleep(5)
    driver.close()

    log.write("STOP: post " + title + " \n")
    log.write("CHECK: post " + title + " \n")
    
    postid = checkpostfacebook(email,password,profileID,title)
    if  postid == "":
        log.write("ERROR: post " + title + " does not exist")
    else:
        log.write("SUCCESS: post " + title + " does exist with postid " + postid)

    log.close()

