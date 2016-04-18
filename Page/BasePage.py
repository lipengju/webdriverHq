#coding:utf-8

from appium import  webdriver
from selenium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import  By
import  time as t

class Factory(object):
	def __init__(self,driver):
		self.driver=driver

	#工厂方法
	def createWebDdriver(self,webDdriver):
		if webDdriver=='web':
			return WebUI(self.driver)
		elif webDdriver=='app':
			return AppUI(self.driver)

class WebDdriver(object):
	def __init__(self,driver):
		self.driver=driver

	def __str__(self):
		return 'webDdriver'

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except NoSuchElementException,e:
			print 'Error details :%s'%(e.args[0])

	def findsElement(self,*loc):
		try:
			return self.driver.find_elements(*loc)
		except NoSuchElementException,e:
			print 'Error details :%s'%(e.args[0])

	@property
	def wait(self):
		t.sleep(2)

	def getScreenshot(self,name,form='png'):
		t.sleep(2)
		self.driver.get_screenshot_as_file('E:/git/localhost/webdriverHq/img/'+name+"."+form)

class WebUI(WebDdriver):
	def __str__(self):
		return 'WEB UI'

class AppUI(WebDdriver):
	def __str__(self):
		return 'App UI'


















