from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PATH = r"C:\Users\your_name\Downloads\chromedriver_win32\chromedriver.exe" #or wherever you save the chrome driver to


driver = webdriver.Chrome(PATH)

driver.get("https://verified.capitalone.com/auth/signin?Product=Card")

name = driver.find_element_by_id('ods-input-0')

name.send_keys("username") #this would be your capital one username

password = driver.find_element_by_id('ods-input-1')

password.send_keys('password') #capital one password


submit = driver.find_element_by_xpath('/html/body/app-root/div/div/app-sign-in/ci-content-card/div/div/ngx-ent-signin/form/p[2]/button')
submit.submit()


