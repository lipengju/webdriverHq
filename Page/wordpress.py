#!/usr/bin/env python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.action_chains import ActionChains
from BasePage import WebUI
from model.Model import DataHelper


class Wordpress(WebUI,DataHelper):
	username_loc=(By.ID,'user_login')
	password_loc=(By.ID,'user_pass')
	login_loc=(By.ID,'wp-submit')
	div_loc=(By.XPATH,".//*[@id='login_error']")
	niCheng_loc=(By.XPATH,".//*[@id='wp-admin-bar-my-account']/a")
	exit_loc=(By.XPATH,".//*[@id='wp-admin-bar-logout']/a")
	exitDiv_loc=(By.CSS_SELECTOR,'.message')

	def typeUserName(self,username):
		self.wait
		self.findElement(*self.username_loc).send_keys(username)

	def typePassword(self,password):
		self.wait
		self.findElement(*self.password_loc).send_keys(password)

	def clickLogin(self):
		self.wait
		self.findElement(*self.login_loc).click()

	def getDiv(self):
		self.wait
		return self.findElement(*self.div_loc).text

	def getNiCheng(self):
		self.wait
		return self.findElement(*self.niCheng_loc).text

	def login(self,parent='wordpress',username='username',password='passwd'):
		self.typeUserName(self.getXmlUser(parent,username))
		self.typePassword(self.getXmlUser(parent,password))
		self.clickLogin()

	def clickExit(self):
		element=self.findElement(*self.niCheng_loc)
		action=ActionChains(self.driver)
		action.move_to_element(element).perform()
		self.wait
		self.findElement(*self.exit_loc).click()

	def getExitDiv(self):
		self.wait
		return self.findElement(*self.exitDiv_loc).text

	'''
	创建文章页面属性元素
	'''
	wenZhang_loc=(By.XPATH,".//*[@id='menu-posts']/a/div[3]")
	xie_loc=(By.XPATH,".//*[@id='wpbody-content']/div[4]/h2/a")
	title_loc=(By.ID,"title")
	publish_loc=(By.ID,'publish')
	allWenZhang_loc=(By.LINK_TEXT,u'所有文章')
	titleLink_loc=(By.LINK_TEXT,'automation')


	def clickWenZhang(self):
		self.wait
		self.findElement(*self.wenZhang_loc).click()

	def clickXie(self):
		self.wait
		self.findElement(*self.xie_loc).click()

	def typeTitle(self,title):
		self.wait
		self.findElement(*self.title_loc).send_keys(title)

	def clickPublish(self):
		self.wait
		self.findElement(*self.publish_loc).click()

	def richText(self,content):
		self.wait
		js="document.getElementById('content_ifr').contentWindow." \
		   "document.body.innerHTML=\"%s\""%(content)
		self.driver.execute_script(js)

	def clickAllWenZhang(self):
		self.wait
		self.findElement(*self.allWenZhang_loc).click()

	def getTitle(self):
		self.wait
		return self.findElement(*self.titleLink_loc).text

	def createWen(self,parent='wen',title='title',content='content'):
		self.clickWenZhang()
		self.clickXie()
		self.typeTitle(self.getXmlUser(parent,title))
		self.richText(self.getXmlUser(parent,content))
		self.clickPublish()


	def isCreateWen(self,value='noWen'):
		try:
			self.clickWenZhang()
			self.delete()
		except:
			self.createWen()
			self.clickAllWenZhang()
		else:
			self.createWen()
			self.clickAllWenZhang()
		finally:
			pass

	'''
	删除文章页面属性
	'''
	removehuishou_loc=(By.CSS_SELECTOR,".submitdelete")
	huishouzhan_loc=(By.XPATH,".//*[@id='wpbody-content']/div[4]/ul/li[2]/a")
	delete_loc=(By.CSS_SELECTOR,"#delete_all")

	def remove(self):
		self.wait
		element=self.findElement(*self.titleLink_loc)
		action=ActionChains(self.driver)
		action.move_to_element(element).perform()

	def clickRemoveHuiShou(self):
		self.wait
		self.findElement(*self.removehuishou_loc).click()

	def clickHuiShouZhan(self):
		self.wait
		self.findElement(*self.huishouzhan_loc).click()

	def clickDelete(self):
		self.wait
		self.findElement(*self.delete_loc).click()

	def delete(self):
		self.remove()
		self.clickRemoveHuiShou()
		self.clickHuiShouZhan()
		self.clickDelete()












