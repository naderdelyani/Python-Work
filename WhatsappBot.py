
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import Select


driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

name = input('Enter Name :')
msg = input ('Enter Message :')
count = int(input('Enter How many Insert Message : '))
input ('Enter Any Key ...')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
txtbox=driver.find_element_by_xpath('//div[contains@class="_2HE1Z _1hRBM"]')
txtbox.click()

msgbox=driver.find_element_by_class_name ('_1awRl')

for i in range (count):
    msgbox.send_keys(msg)
    try:
        button = driver.find_element_by_class_name('_2Ujuu')
        button.click()
    except NoSuchElementException:
        pass



    






