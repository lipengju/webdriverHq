#!/usr/bin/env python
#coding:utf-8

import  unittest
from appium import  webdriver
from Page.basetestcase import  AppTestCase
from model.Model import  DataHelper
from Page.weixin import WeiXin
import  time as t



class weixinTest(AppTestCase,WeiXin):

	def test_001(self):
		'''点击登陆，输入微信的用户名和密码'''
		self.login()

	def test_002(self):
		'''进入到微信的公众号'''
		self.login()
		self.clickTong()
		self.clickGong()
		t.sleep(5)
		self.clickTing()
		t.sleep(4)

	def test_003(self):
		'''点击停车王的个人中心'''
		self.login()
		self.gz()
		self.clickGeRen()
		t.sleep(3)
		self.clickZhongXin()
		t.sleep(6)

	def test_004(self):
		'''点击我的车牌'''
		self.login()
		self.gz()
		self.clickGeRen()
		t.sleep(3)
		self.clickZhongXin()
		t.sleep(6)
		self.clickChe()
		t.sleep(5)

	def test_005(self):
		'''在我的车牌-绑定手机号输入框输入手机号码'''
		self.login()
		self.gz()
		self.clickGeRen()
		t.sleep(3)
		self.clickZhongXin()
		t.sleep(6)
		self.clickChe()
		t.sleep(5)
		self.typePhone()
		self.clickFa()
		t.sleep(6)

	def test_006(self):
		'''获取停车场的名称'''
		self.login()
		self.gz()
		self.assertEqual(self.getTingChe(),u'停车场')

	def test_007(self):
		'''点击停车场'''
		self.login()
		self.gz()
		self.clickTingChe()
		t.sleep(6)

	def test_008(self):
		'''停车场输入搜索的地址'''
		self.login()
		self.gz()
		self.clickTingChe()
		t.sleep(6)

if __name__=='__main__':
	unittest.main(verbosity=2)
