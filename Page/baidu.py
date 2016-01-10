#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import  By
from homePage import  HomePage
from BasePage import WebUI


class BaiduPage(WebUI):
	click_loc=(By.XPATH,".//*[@id='u1']/a[7]")
	userName_loc=(By.ID,'TANGRAM__PSP_8__userName')
	password_loc=(By.ID,'TANGRAM__PSP_8__password')
	clickButton_loc=(By.ID,'TANGRAM__PSP_8__submit')
	error_loc=(By.XPATH,".//*[@id='TANGRAM__PSP_8__error']")


	def click(self):
		self.wait
		self.findElement(*self.click_loc).click()

	def getUserTextField(self,username):
		self.wait
		self.findElement(*self.userName_loc).send_keys(username)

	def getPasswordField(self,password):
		self.wait
		self.findElement(*self.password_loc).send_keys(password)

	def getSubmitButton(self):
		self.wait
		self.findElement(*self.clickButton_loc).click()

	def getLoginErrorDiv(self):
		self.wait
		return self.findElement(*self.error_loc).text

	def login(self,username,password):
		self.doLogin(username,password)
		return HomePage(self.driver)

	def doLogin(self,username,password):
		self.click()
		self.getUserTextField(username)
		self.getPasswordField(password)
		self.getSubmitButton()





