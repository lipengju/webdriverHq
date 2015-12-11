#coding:utf-8

from model import  Model

def main():
	username=raw_input(u'请输入用户名:\n')
	passwd=raw_input(u'请输入地址:\n')
	user=Model.User()
	result=user.checkValidate(username,passwd)
	if not result:
		print u'用户验证失败'
	else:
		print u'用户注册成功，欢迎进入XX系统!'

if __name__=='__main__':
	main()