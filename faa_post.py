from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import selenium
import sys

#
# post an image under faa with selenium
#
def faa_post(username, password, userid, title, imagepathfile, description, tags):

    driver = webdriver.Firefox()
    driver.get("https://fineartamerica.com/loginartist.php")

    elem = driver.find_element_by_name("username")
    elem.send_keys(username)
    elem.send_keys(Keys.RETURN)
    elem = driver.find_element_by_name("password")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    driver.get("http://fineartamerica.com/profiles/" + userid + ".html")

    element = driver.find_element(By.PARTIAL_LINK_TEXT, "Upload Image")
    element.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "uploadimage"))
        )
        driver.find_element_by_css_selector("input[type=\"file\"]").send_keys(imagepathfile)

    finally:
        print "error"

    element = driver.find_element(By.PARTIAL_LINK_TEXT, "Upload Image")
    element.click()

    try:
        element = WebDriverWait(driver, 1000).until(
            EC.presence_of_element_located((By.NAME, "artworkname"))
        )

        artworkname = title
        artworkkeywords = tags
        artworkdescription = description

        elem = driver.find_element_by_name("artworkname")
        elem.send_keys(artworkname)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("artworkkeywords")
        elem.send_keys(artworkkeywords)
        elem.send_keys(Keys.RETURN)
        elem = driver.find_element_by_name("artworkdescription")
        elem.send_keys(artworkdescription)
        elem.send_keys(Keys.RETURN)

        element = driver.find_element(By.PARTIAL_LINK_TEXT, "Submit")
        element.click()

    finally:
        driver.close()


