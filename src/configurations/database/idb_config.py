from abc import ABC,abstractmethod

class IDbConfig(ABC):
	def __init__(self,host,database,user,password,charset):
		self.host=host
		self.database=database
		self.user=user
		self.password=password
		self.charset=charset

	@abstractmethod
	def connection(self):
		pass

	@abstractmethod
	def run_query(self,query):
		pass