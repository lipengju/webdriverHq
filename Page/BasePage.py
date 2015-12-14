#coding:utf-8

from selenium import  webdriver
from appium import  webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import  By
import  time as t


class Page(object):
	def __init__(self,driver):
		self.driver=driver

	def find_element(self,*loc):
		try:
			return  self.driver.find_element(*loc)
		except (NoSuchElementException,KeyError,ValueError,Exception),e:
			print 'Error details:%s'%(e.args[0])

	@property
	def wait(self):
		t.sleep(2)

















