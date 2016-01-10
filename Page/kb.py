#coding:utf-8

from appium import  webdriver
from selenium.webdriver.common.by import By
from Page.BasePage import AppUI
import  time as  t

class KouBei(AppUI):
	address_loc=(By.ID,'com.taobao.mobile.dipei:id/waimai_start_button')
	my_loc=(By.NAME,u'我的')
	login_loc=(By.ID,'com.taobao.mobile.dipei:id/ddt_login_title')
	loginDiv_loc=(By.ID,'com.taobao.mobile.dipei:id/title_bar_back_button')
	username_loc=(By.ID,'com.taobao.mobile.dipei:id/accountCompleteTextView')
	password_loc=(By.ID,'com.taobao.mobile.dipei:id/content')
	loginButton_loc=(By.ID,'com.taobao.mobile.dipei:id/loginButton')

	def clickAddress(self):
		self.wait
		self.findElement(*self.address_loc).click()
		t.sleep(6)

	def clickMy(self):
		self.wait
		self.findElement(*self.my_loc).click()

	def clicklogin(self):
		self.wait
		self.findElement(*self.login_loc).click()

	def getLoginDiv(self):
		self.wait
		return self.findElement(*self.loginDiv_loc).text

	def getUsername(self,username):
		self.wait
		self.findElement(*self.username_loc).send_keys(username)

	def getPassword(self,password):
		self.wait
		self.findElement(*self.password_loc).send_keys(password)

	def clickLoginButton(self):
		self.wait
		self.findElement(*self.loginButton_loc).click()

	def login(self,username,password):
		self.clickMy()
		self.clicklogin()
		self.getUsername(username)
		self.getPassword(password)
		self.clickLoginButton()