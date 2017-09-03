#!/usr/bin/env python
#coding:utf-8

import  unittest
from Page.basetestcase import BaseTestCase
from model.Model import DataHelper
from Page.wordpress import Wordpress

class WordpressPage(BaseTestCase,Wordpress):

	def test_001(self,value='passwd'):
		'''测试：用户名正确密码错误'''
		self.login('admin','assdf')
		self.assertEqual(self.getDiv(),self.getXmlData(value))

	def test_002(self,value='userDiv'):
		'''测试：用户名密码都错误'''
		self.login('aaa','admin')
		self.assertEqual(self.getDiv(),self.getXmlData(value))

	def test_003(self,parent='wordpress',username='username'):
		'''测试：wordpress登录成功'''
		self.login()
		self.assertTrue(self.driver.current_url.endswith('wp-admin/'))
		self.assertTrue(self.getNiCheng().endswith(self.getXmlUser(parent,username)))

	def test_004(self,parent='wen',title='title'):
		'''测试:wordpress创建文章'''
		self.login()
		self.isCreateWen()
		self.assertEqual(self.getTitle(),self.getXmlUser(parent,title))
		self.delete()

	def test_005(self,value='exit'):
		'''测试:退出系统'''
		self.login()
		self.clickExit()
		self.assertEqual(self.getExitDiv(),self.getXmlData(value))

if __name__=='__main__':
	unittest.main(verbosity=2)
