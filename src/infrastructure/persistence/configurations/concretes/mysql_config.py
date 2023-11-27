import pymysql

class MySQLConfig():
	def __init__(self,host,database,user,password,charset="utf8mb4"):
		super().__init__(host,database,user,password,charset)
		self.cursorclass=pymysql.cursors.DictCursor

	def connection(self):
		self.conn=pymysql.connect(
			host=self.host,
			database=self.database,
			user=self.user,
			password=self.password,
			charset=self.charset,
			cursorclass=self.cursorclass
		)
		cursor=self.conn.cursor()
		return cursor
	
	def run_query(self,query)->bool:
		cursor=self.connection()
		cursor.execute(query)
		result=cursor.fetchall()
		self.conn.close()
		return result