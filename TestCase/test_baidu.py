#coding:utf-8

import  unittest
from Page.basetestcase import BaseTestCase
from Page.baidu import  BaiduPage
from model import Model
from ddt import  ddt,data,unpack


@ddt
class baiduPage(BaseTestCase,BaiduPage):

	@data(*Model.DataHelper().readExcels())
	@unpack
	def testLogin_001(self,username,password,context_expxcted):
		'''测试：百度登录失败的N种情况'''
		self.doLogin(username,password)
		self.assertEqual(context_expxcted,self.getLoginErrorDiv())

if __name__=='__main__':
	unittest.main(verbosity=2)
