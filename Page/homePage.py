#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import  By
from BasePage import  Page

class HomePage(Page):
	niCheng_loc=(By.CSS_SELECTOR,'.user-name')

	def getNiCheng(self):
		self.wait
		return self.find_element(*self.niCheng_loc).text