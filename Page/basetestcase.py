#!/usr/bin/env python
#coding:utf-8

import unittest
from appium import  webdriver
from selenium import webdriver
import  os

PATH=lambda p:os.path.abspath(
	os.path.join(os.path.dirname(__file__),p)
)


class BaseTestCase(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.get('http://localhost/wordpress/wp-login.php')
		self.driver.implicitly_wait(30)

	def tearDown(self):
		self.driver.quit()

class AppTestCase(unittest.TestCase):
	def setUp(self):
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']='4.4.4'
		desired_caps['deviceName']='m2'
		# desired_caps['appPackage']='Package name:com.tencent.mm'
		# desired_caps['appActivity']='com.tencent.mm.ui.LauncherUI'
		# desired_caps['unicodeKeyboard']=True
		# desired_caps['resetKeyboard']=True
		desired_caps['app']=PATH('C:\\weixin6331android940.apk')
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

	def tearDown(self):
		self.driver.quit()