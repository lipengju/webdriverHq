#coding:utf-8

from selenium import  webdriver
import  time as t

driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get('http://www.126.com/')
driver.switch_to_frame('x-URS-iframe')
t.sleep(3)
driver.find_element_by_name('email').send_keys('weiketest')
t.sleep(3)
driver.find_element_by_id('dologin').click()
t.sleep(3)
print driver.find_element_by_xpath(".//*[@class='ferrorhead']").text
driver.execute_script()
driver.close()
