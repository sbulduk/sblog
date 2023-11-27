import pymysql

class DbConfig():
	def __init__(self,host="sql11.freesqldatabase.com",database="sql11665351",user="sql11665351",password="BnzhzFlJYd",charset="utf8mb4"):
		self.host=host
		self.database=database
		self.user=user
		self.password=password
		self.charset=charset
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
	
if(__name__=="__main__"):
	a=Db_Config()
	res=a.run_query("select * from users")
	if(res):
		for row in res:
			print(f"{row['id']}\t{row['email']}")
	else:
		print(f"No rows found!")