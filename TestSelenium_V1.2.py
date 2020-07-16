from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time 
u = str(input("your url:"))
def Chottomatte(usernamess2,url):
    browser =  webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    username = browser.find_element_by_id('user-name')
    password = browser.find_element_by_id('user-password')
    submit = browser.find_element_by_name('submit')

    username.send_keys(usernamess2)
    password.send_keys(f'Debsirin{usernamess2}')
    submit.click()

    profile = browser.find_element_by_class_name('round')
    
    time.sleep(3)
    
    browser.close()
user = ['46068','46012']
for i in user:
    Chottomatte(i,u)

#made by Punnawat DebsririnSchool มีปัญหาหรือผิดกฏอยากคุยทักได้:)



