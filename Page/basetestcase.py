#coding:utf-8

import unittest
from appium import  webdriver
from selenium import webdriver

class BaseTestCase(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get('http://www.baidu.com')
		self.driver.implicitly_wait(30)

	def tearDown(self):
		self.driver.quit()

class AppTestCase(unittest.TestCase):
	def setUp(self):
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']='4.4.4'
		desired_caps['deviceName']='Samsung Galaxy S4-4.4.4'
		desired_caps['appPackage']='com.taobao.mobile.dipei'
		desired_caps['appActivity']='com.taobao.ecoupon.activity.PortalActivity'
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

	def tearDown(self):
		self.driver.quit()