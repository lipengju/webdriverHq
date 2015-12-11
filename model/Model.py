#coding:utf-8

import  os,csv,xlrd
import  xml.dom.minidom
import sqlite3
import  MySQLdb
import  config


class Config(object):
	def __init__(self):
		pass

	@staticmethod
	def data_dirs():
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		DATA_DIRS = (
		os.path.join(BASE_DIR,  'Data-Driven'),
		)
		d='/'.join(DATA_DIRS)
		return d


class DataHelper(object):
	def __init__(self):
		pass

	def getList(self):
		list=[['','',u'请您填写手机/邮箱/用户名'],['admin','',u'请您填写密码'],['admin','admin',u'请输入验证码']]
		return list

	def readFile(self,index):
		f=open(Config.data_dirs()+'/system.txt','r')
		d=f.readlines()
		f.close()
		return d[index]

	def readCsv(self,value1,value2):
		rows=[]
		data_file=open(Config.data_dirs()+'/system.csv')
		reader=csv.reader(data_file)
		next(reader,None)
		for row in reader:
			rows.append(row)
		return ''.join(rows[value1][value2]).decode('gb2312')

	def readExcel(self,rowValue,colValue):
		book=xlrd.open_workbook(Config.data_dirs()+'/system.xlsx')
		sheet=book.sheet_by_index(0)
		return sheet.cell_value(rowValue,colValue)

	def readExcels(self):
		rows=[]
		book=xlrd.open_workbook(Config.data_dirs()+'/system.xlsx')
		sheet=book.sheet_by_index(0)
		for row in range(1,sheet.nrows):
			rows.append(list(sheet.row_values(row,0,sheet.ncols)))
		return rows

	def getXmlData(self,value):
		dom=xml.dom.minidom.parse(Config.data_dirs()+"/system.xml")
		db=dom.documentElement
		name=db.getElementsByTagName(value)
		nameValue=name[0]
		return nameValue.firstChild.data

	def getXmlUser(self,parent,child):
		dom=xml.dom.minidom.parse(Config.data_dirs()+"/system.xml")
		db=dom.documentElement
		itemlist=db.getElementsByTagName(parent)
		item=itemlist[0]
		return item.getAttribute(child)

class SqliteHelper(object):

	def selectSqlite(self,value1,value2):
		rows=[]
		try:
			conn=sqlite3.connect(Config.data_dirs()+'/mydatabase.db')
			cur=conn.cursor()
			sql="select *  from element"
			cur.execute(sql)
			data=cur.fetchall()
			for d in data:
				rows.append(d)
			return rows[value1][value2]
		except:
			print u'操作sqlite3数据库失败'
		finally:
			cur.close()
			conn.close()

class MySQLHelper(object):
	def __init__(self):
		self.__conn=config.conn

	def selectMySQL(self,index1,index2):
		rows=[]
		try:
			conn=MySQLdb.connect(**self.__conn)
			cur=conn.cursor()
		except Exception,e:
			print u'操作mysql数据库失败'
		else:
			cur.execute('select *  from element')
			data=cur.fetchall()
			for d in data:
				rows.append(d)
			return rows[index1][index2]
		finally:
			cur.close()
			conn.close()

	def get_One(self,sql,params):
		try:
			conn=MySQLdb.connect(**self.__conn)
			cur=conn.cursor()
			reCount=cur.execute(sql,params)
			data=cur.fetchone()
			return data
		except:
			print u'操作数据库失败'
		finally:
			cur.close()
			conn.close()

	def insertMySQL(self,sql,params):
		try:
			conn=MySQLdb.connect(**self.__conn)
			cur=conn.cursor()
			cur.execute(sql,params)
			conn.commit()
		except Exception,e:
			print u'操作mysql数据库失败'
		finally:
			cur.close()
			conn.close()

class User(object):
	def __init__(self):
		self.__helper=MySQLHelper()

	def get_One(self,id):
		sql='select *  from account where id=%s'
		params=(id,)
		return self.__helper.get_One(sql,params)

	def checkValidate(self,name,address):
		sql='select * from account where username=%s and passwd=%s'
		params=(name,address,)
		return self.__helper.get_One(sql,params)
#
if __name__=='__main__':
	per=MySQLHelper()
	print per.selectMySQL2()
