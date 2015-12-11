#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time as t

#等待方法
def wait():
	t.sleep(2)

def clickLogin(driver):
	wait()
	driver.find_element_by_id('u1').find_element_by_class_name('lb').click()

def typeUsername(driver,username):
	clickLogin(driver)
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__userName').send_keys(username)

def typePassword(driver,password):
	clickLogin(driver)
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__password').send_keys(password)

def clickButtonLogin(driver):
	wait()
	driver.find_element_by_id('TANGRAM__PSP_8__submit').click()


def getErrorText(driver):
	wait()
	return  driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_8__error']").text

#登录方法
def login(driver,username,password):
	clickLogin(driver)
	typeUsername(driver,username)
	typePassword(driver,password)
	clickButtonLogin(driver)

#获取昵称方法
def getNiCheng(driver):
	wait()
	return driver.find_element_by_css_selector("#s_username_top > span").text




