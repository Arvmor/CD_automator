from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# or wherever you save the chrome driver to
PATH = r"C:\Users\your_name\Downloads\chromedriver_win32\chromedriver.exe"


driver = webdriver.Chrome(PATH)

driver.get("https://verified.capitalone.com/auth/signin?Product=Card")

# this would be your capital one username
driver.find_element_by_id('ods-input-0').send_keys("username")
time.sleep(2)
driver.find_element_by_id(
    'ods-input-1').send_keys('password')  # capital one password
time.sleep(2)
driver.find_element_by_xpath(
    '/html/body/app-root/div/div/app-sign-in/ci-content-card/div/div/ngx-ent-signin/form/p[2]/button').click()
