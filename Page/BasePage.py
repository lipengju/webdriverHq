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

	@property
	def wait(self):
		t.sleep(2)

	@property
	def getHeight(self):
		self.wait
		return self.driver.get_window_size()['height']

	@property
	def getWidth(self):
		self.wait
		return self.driver.get_window_size()['width']

	@property
	def getResolution(self):
		'''
		:return:获取屏幕的分辨率
		'''
		return self.getHeight*self.getWidth

	@property
	def setDownUp(self):
		'''
		:return:实现从下往上滑动
		'''
		self.driver.swipe(self.getWidth/2,self.getHeight/20,self.getWidth/2,self.getHeight*9/10,0)
		self.wait

	@property
	def setUpDown(self):
		'''
		:return:实现从上往下滑动
		'''
		self.driver.swipe(self.getWidth/2,self.getHeight*9/10,self.getWidth/2,self.getHeight/20,0)
		self.wait

	@property
	def setLeftRight(self):
		'''
		:return: 实现从左到右滑动
		'''
		self.driver.swipe(self.getWidth*9/10,self.getHeight/2,self.getWidth/20,self.getHeight/2,0)
		self.wait

	@property
	def setRightLeft(self):
		'''
		:return:实现从右到左滑动
		'''
		self.driver.swipe(self.getWidth/10,self.getHeight/2,self.getWidth*9/10,self.getHeight/2,0)
		self.wait

	@property
	def getScreenshot(self):
		self.wait
		nowTime=t.strftime('%Y-%m-%d %H_%M_%S',t.localtime())
		self.driver.get_screenshot_as_file(nowTime+'.png')


class WebUI(WebDdriver):
	def __str__(self):
		return 'WEB UI'

class AppUI(WebDdriver):
	def __str__(self):
		return 'App UI'


















