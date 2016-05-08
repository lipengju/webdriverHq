#coding:utf-8

from appium import  webdriver
from selenium.webdriver.common.by import By
from Page.BasePage import AppUI

class KouBei(AppUI):
	sure_loc=(By.ID,'android:id/button3')
	mai_loc=(By.NAME,u'外卖')

	def clickSure(self):
		self.wait
		self.wait
		self.findElement(*self.sure_loc).click()

	def getMai(self):
		self.wait
		self.wait
		return self.findElement(*self.mai_loc).text
