#!usr/bin/env python
#!coding:utf-8

from appium import  webdriver
import  time as t
import  os


class Swipe(object):
	def __init__(self,driver):
		self.driver=driver

	@property
	def width(self):
		return self.driver.get_window_size()['width']

	@property
	def height(self):
		return  self.driver.get_window_size()['height']

	@property
	def getResolution(self):
		return str(self.width)+"*"+str(self.height)

	@property
	def set_Left_Right(self):
		'''
		:return: 实现从左到右滑动,滑动时X轴起点大于终点
		'''
		t.sleep(2)
		self.driver.swipe(self.width*9/10,self.height/2,self.width/20,self.height/2,0)

	@property
	def set_Right_Left(self):
		'''
		:return:实现从右到左滑动,滑动时X轴起点小于终点
		'''
		t.sleep(2)
		self.driver.swipe(self.width/10,self.height/2,self.width*9/10,self.height/2,0)

	@property
	def set_Up_Down(self):
		'''
		:return: 实现从上往下滑动,滑动时Y轴起点起点大于终点
		'''
		t.sleep(2)
		self.driver.swipe(self.width/2,self.height*9/10,self.width/2,self.height/20,0)

	@property
	def set_Down_Up(self):
		'''
		:return: 实现从下往上滑动,滑动时Y轴起点小于终点
		'''
		t.sleep(2)
		self.driver.swipe(self.width/2,self.height/20,self.width/2,self.height*9/10,0)












