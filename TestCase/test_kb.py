#coding:utf-8

import  unittest
from appium import  webdriver
from Page.kb import KouBei
from Page.basetestcase import AppTestCase
from model import Model
from model.Model import DataHelper

class KouBeiTest(AppTestCase,KouBei):

	def testLogin(self,value='mai'):
		'''验证跳转到外卖的首页'''
		db=DataHelper()
		self.clickSure()
		self.assertEqual(self.getMai(),db.getXmlData(value))

if __name__=='__main__':
	unittest.main(verbosity=2)

