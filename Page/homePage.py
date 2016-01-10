#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import  By
from BasePage import  WebUI

class HomePage(WebUI):
	niCheng_loc=(By.CSS_SELECTOR,'.user-name')

	def getNiCheng(self):
		self.wait
		return self.find_element(*self.niCheng_loc).text