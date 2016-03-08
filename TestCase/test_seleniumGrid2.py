#coding:utf-8

from selenium import  webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time as t

listBrowser=['firefox','chrome']

for browser in listBrowser:
	driver=webdriver.Remote(
		'http://127.0.0.1:4444/wd/hub',
		desired_capabilities={
			'browserName':browser,
			'platform':'ANY',
			'version':'',
			'javascriptEnabled':True
		}
	)
	print u'目前测试的浏览器为:',browser
	driver.get('http://www.baidu.com')
	t.sleep(3)
	driver.find_element_by_id('kw').send_keys('selenium grid2')
	driver.close()








