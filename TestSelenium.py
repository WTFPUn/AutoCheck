from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time 

def Chottomatte(usernamess2):
    browser =  webdriver.Chrome('chromedriver.exe')
    browser.get('https://checkin.debsirin.online/login.php')
    username = browser.find_element_by_id('user-name')
    password = browser.find_element_by_id('user-password')
    submit = browser.find_element_by_name('submit')

    username.send_keys(usernamess2)
    password.send_keys(f'Debsirin{usernamess2}')
    submit.click()

    profile = browser.find_element_by_class_name('round')
    #logout  = browser.find_element_by_partial_link_text('https://checkin.debsirin.online/authentication-module/logout.php')
    # profile.click()
    # logout.click()
    time.sleep(3)
    
    browser.close()
user = ['46068','46081','46012']
for i in user:
    Chottomatte(i)

#made by Punnawat DebsririnSchool มีปัญหาหรือผิดกฏอยากคุยทักได้:)



