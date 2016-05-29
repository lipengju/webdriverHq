#coding:utf-8
import unittest
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
import  os
import  time as t
PATH=lambda p:os.path.abspath(
	os.path.join(os.path.dirname(__file__),p)
)

class AppTestCase(unittest.TestCase):
	def setUp(self):
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']='4.4.4'
		desired_caps['deviceName']='m2'
		desired_caps['unicodeKeyboard']=True
		desired_caps['resetKeyboard']=True
		desired_caps['app']=PATH('C:\\d2465abab2023b8b21a56141465c7925.apk')
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

	def test_001(self):
		'''获取手机的分辨率'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		print u'手机的分辨率为:',width,'*',height

	def test_002(self):
		'''实现从左至右滑动'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		t.sleep(5)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/first.png')
		t.sleep(5)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/second.png')

	def test_003(self):
		'''实现从右至至滑动'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		t.sleep(5)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/first.png')
		t.sleep(5)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/second.png')
		t.sleep(5)
		self.driver.swipe(width/10,height/2,width*9/10,height/2,0)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/three.png')

	def test_004(self):
		'''实现从下至上滑动'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		t.sleep(5)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		t.sleep(2)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		t.sleep(2)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		t.sleep(2)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/index.png')
		t.sleep(6)
		self.driver.swipe(width/2,height*9/10,width/2,height/20,0)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/down.png')
		t.sleep(6)
		self.driver.swipe(width/2,height/20,width/2,height*9/10,0)
		self.driver.get_screenshot_as_file('D:/git/Python/webdriverHq/img/up.png')

	def test_005(self):
		'''验证long_press方法'''
		width=self.driver.get_window_size()['width']
		height=self.driver.get_window_size()['height']
		t.sleep(5)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		t.sleep(2)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		t.sleep(2)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		t.sleep(2)
		self.driver.swipe(width*9/10,height/2,width/20,height/2,0)
		touch=TouchAction(self.driver)
		t.sleep(5)
		element=self.driver.find_element_by_id('com.baozoumanhua.android:id/channel_tv')
		touch.long_press(element).perform()
		t.sleep(4)
		actual_text=self.driver.find_element_by_id('com.baozoumanhua.android:id/tv_channel_title').text
		self.assertEqual(actual_text,u'暴走大事件第四季')


	def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main(verbosity=2)