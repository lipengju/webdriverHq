#coding:utf-8

conn=dict(host='127.0.0.1',user='root',passwd='server',db='db',charset='utf8')


def getConfig():
	list={
		'http://127.0.0.1:5555/wd/hub':'chrome',
		'http://127.0.0.1:5556/wd/hub':'firefox',
	}
	print u'获取终端和浏览器成功！！'
	return list