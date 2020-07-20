from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time 


import datetime
day =str(datetime.date.today()).replace("-","")


import sqlite3
conn = sqlite3.connect('Url_table.db')
c = conn.cursor()
# exe = c.execute(f"SELECT one FROM url WHERE Day == {day} ;")
# rows = c.fetchone()
# u = rows[0]


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
user = ['46081','46012','46020','46048','46013']

# for i in user:
    #Chottomatte(i,u)

timel = ["8:11:10","9:02:50","9:51:20","11:01:20","11:51:20","12:41:20","13:31:20","14:21:20","15:11:20","16:01:20"]
d = ['one','two','three','four','five','six','seven','eight','nine']
while True :
    tim = str(datetime.datetime.now())[12:19]
    for i in range(9):
        if  timel[i] == tim :
            exe = c.execute(f"SELECT {d[i]} FROM url WHERE Day == {day} ;")
            rows = c.fetchone()
            u = rows[0]
            for j in user:
                Chottomatte(j,u)
                print(f'Check : {j} complete!')
    print(f". . . running . . .({tim})")
    time.sleep(1)


#made by Punnawat DebsririnSchool มีปัญหาหรือผิดกฏอยากคุยทักได้:)



