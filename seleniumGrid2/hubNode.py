#coding:utf-8

from selenium import  webdriver
from threading import  Thread
import  time as t
from model.config import  getConfig

class MyThread(Thread):
	def run(self):
		Thread.run(self)

def  testBaidu(host,browser):
	print host,browser
	driver=webdriver.Remote(
		command_executor=host,
		desired_capabilities={
			'platform':'ANY',
			'browserName':browser,
			'version':'',
			'javascriptEnabled':True
		}
	)
	driver.get('http://www.baidu.com')
	driver.find_element_by_id('kw').send_keys('grid2')
	t.sleep(2)
	driver.close()

threads=[]
files=range(len(getConfig()))

for host,browser in getConfig().items():
	t1= MyThread(target=test_baidu,args=(host,browser))
	threads.append(t1)

if __name__=='__main__':
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()
	print 'Over'