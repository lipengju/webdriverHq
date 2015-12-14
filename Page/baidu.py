#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import  By
from BasePage import  Page
from homePage import  HomePage


class BaiduPage(Page):
	click_loc=(By.XPATH,".//*[@id='u1']/a[7]")
	userName_loc=(By.ID,'TANGRAM__PSP_8__userName')
	password_loc=(By.ID,'TANGRAM__PSP_8__password')
	clickButton_loc=(By.ID,'TANGRAM__PSP_8__submit')
	error_loc=(By.XPATH,".//*[@id='TANGRAM__PSP_8__error']")


	def click(self):
		self.wait
		self.find_element(*self.click_loc).click()

	def getUserTextField(self,username):
		self.wait
		self.find_element(*self.userName_loc).send_keys(username)

	def getPasswordField(self,password):
		self.wait
		self.find_element(*self.password_loc).send_keys(password)

	def getSubmitButton(self):
		self.wait
		self.find_element(*self.clickButton_loc).click()

	def getLoginErrorDiv(self):
		self.wait
		return self.find_element(*self.error_loc).text

	def login(self,username,password):
		self.doLogin(username,password)
		return HomePage(self.driver)

	def doLogin(self,username,password):
		self.click()
		self.getUserTextField(username)
		self.getPasswordField(password)
		self.getSubmitButton()





