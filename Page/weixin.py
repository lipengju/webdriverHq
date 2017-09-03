#!/usr/bin/env python
#coding:utf-8

from appium import  webdriver
from selenium.webdriver.common.by import By
from Page.BasePage import AppUI
import  time as t

class WeiXin(AppUI):
	login_loc=(By.ID,'com.tencent.mm:id/ca4')
	qita_loc=(By.ID,'com.tencent.mm:id/bb3')
	username_loc=(By.ID,"com.tencent.mm:id/boq")
	password_loc=(By.ID,"com.tencent.mm:id/g_")
	loginButton_loc=(By.ID,'com.tencent.mm:id/a_m')
	fu_loc=(By.ID,'com.tencent.mm:id/boa')

	def clickLogin(self):
		self.wait
		return self.findElement(*self.login_loc).click()

	def clickQiTa(self):
		self.wait
		return self.findElement(*self.qita_loc).click()

	def typeUsername(self,username):
		'''输入用户名'''
		self.wait
		user=self.findElement(*self.username_loc)
		user.clear()
		self.wait
		user.send_keys(username)

	def typePassword(self,password):
		'''输入密码'''
		self.wait
		passwd=self.findElement(*self.password_loc)
		passwd.clear()
		passwd.send_keys(password)

	def clickLoginButton(self):
		self.wait
		return self.findElement(*self.loginButton_loc).click()

	def clickNot(self):
		self.wait
		self.findElement(*self.fu_loc).click()

	def login(self,username='13484545195',password='1949358810lwp'):
		self.clickLogin()
		self.typeUsername(username)
		self.wait
		self.typePassword(password)
		self.clickLoginButton()
		t.sleep(10)
		self.clickNot()
		t.sleep(10)

	'''微信登录成功后的操作'''
	tong_loc=(By.NAME,u"通讯录")
	gong_loc=(By.XPATH,"//android.widget.TextView[@text='公众号']")
	ting_loc=(By.NAME,u'停车王')

	def clickTong(self):
		self.wait
		self.findElement(*self.tong_loc).click()

	def clickGong(self):
		self.wait
		self.findElement(*self.gong_loc).click()

	def clickTing(self):
		'''点击停车王'''
		self.wait
		self.findElement(*self.ting_loc).click()

	def gz(self):
		self.clickTong()
		self.clickGong()
		self.clickTing()


	'''进入到停车王的操作'''
	geren_loc=(By.NAME,u'个人中心')
	zhongxin_loc=(By.XPATH,"//android.widget.TextView[@index='0']")
	niCheng_loc=(By.XPATH,"//android.view.View[@index='0']")
	che_loc=(By.XPATH,"//android.view.View[@index='2']")

	def clickGeRen(self):
		self.wait
		self.findElement(*self.geren_loc).click()

	def clickZhongXin(self):
		self.wait
		self.findElement(*self.zhongxin_loc).click()

	def getNiCheng(self):
		self.wait
		return self.findElement(*self.niCheng_loc).text

	def clickChe(self):
		self.wait
		self.findElement(*self.che_loc).click()

	def getChe(self):
		self.wait
		return self.findElement(*self.che_loc).text

	'''我的车牌-绑定手机'''
	phone_loc=(By.XPATH,"//android.widget.EditText[@index='1']")
	fa_loc=(By.XPATH,"//android.view.View[@index='2']")

	def typePhone(self,phone='13484545195'):
		self.wait
		self.findElement(*self.phone_loc).send_keys(phone)

	def clickFa(self):
		self.wait
		self.findElement(*self.fa_loc).click()


	'''停车场'''
	tingche_loc=(By.NAME,u'停车场')

	def clickTingChe(self):
		self.wait
		self.findElement(*self.tingche_loc).click()

	def getTingChe(self):
		self.wait
		return self.findElement(*self.tingche_loc).text
















