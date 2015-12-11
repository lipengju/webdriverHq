#coding:utf-8

import  unittest
from Page import  baidu
from model import Model
from Page import  basetestcase


class baiduPage(basetestcase.BaseTestCase):

	def testFailLogin_001(self):
		'''验证：用户名密码名为空，点击登录返回的错误信息'''
		mysql=Model.MySQLHelper()
		baidu.login(self.driver,mysql.selectMySQL(0,0),mysql.selectMySQL(0,1))
		self.assertEqual(mysql.selectMySQL(0,2),baidu.getErrorText(self.driver))

	def testFailLogin_002(self):
		'''验证：只输入用户名，点击登录返回的错误信息'''
		mysql=Model.MySQLHelper()
		baidu.login(self.driver,mysql.selectMySQL(1,0),mysql.selectMySQL(1,1))
		self.assertEqual(mysql.selectMySQL(1,2),baidu.getErrorText(self.driver))


	def testFailLogin_003(self):
		'''验证：用户名密码为空，点击登录返回的错误信息'''
		mysql=Model.MySQLHelper()
		baidu.login(self.driver,mysql.selectMySQL(2,0),mysql.selectMySQL(2,1))
		self.assertEqual(mysql.selectMySQL(2,2),baidu.getErrorText(self.driver))

if __name__=='__main__':
	unittest.main(verbosity=2)
