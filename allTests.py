#coding:utf-8
import  unittest,os,sys,HTMLTestRunner,time
reload(sys)
sys.setdefaultencoding('utf-8')


def suite():
	dir_case=unittest.defaultTestLoader.discover(
		'D:/git/python/webdriverHq/TestCase',
		pattern='test_*.py',
		top_level_dir=None
	)
	return dir_case

def getNowTime():
	return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))


def runAutomation():
	filename='D:/git/python/webdriverHq/Report/'+getNowTime()+'TestReport.html'
	fp=file(filename,'wb')
	runner=HTMLTestRunner.HTMLTestRunner(
		stream=fp,
		title=u'自动化测试报告',
		description=u'自动化测试报告详细的信息'
	)
	runner.run(suite())

if __name__=='__main__':
	runAutomation()