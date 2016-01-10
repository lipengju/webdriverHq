#coding:utf-8

import  unittest
from appium import  webdriver
from selenium import  webdriver
from Page.kb import KouBei
from Page.basetestcase import AppTestCase
from model import Model
from model.Model import DataHelper

class KouBeiTest(AppTestCase,KouBei):

	def testLogin(self,value='kb'):
		'''验证点击选择送地址跳转到登录页面'''
		db=DataHelper()
		self.clickAddress()
		self.assertEqual(db.getXmlData(value),self.getLoginDiv())

if __name__=='__main__':
	unittest.main(verbosity=2)

