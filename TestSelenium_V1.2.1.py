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
    
    time.sleep(0.5)
    
    browser.close()
user = ['46081','46012','46020','46048','46056','46024','46068','46060','46216','46103','46013','46036','46053','46215','46218','46028','46041','46057']
for i in user:
    Chottomatte(i,u)
    print(f'Check :{i} complete')

#made by Punnawat DebsririnSchool มีปัญหาหรือผิดกฏอยากคุยทักได้:)



