from flask import Flask
from controllers import index,posts

class App:
	def __init__(self)->None:
		self.app=Flask(__name__)
		self.configure_routes()

	def configure_routes(self)->None:
		index.configure_routes(self.app)
		posts.configure_routes(self.app)

	def run(self,host="localhost",port="5000"):
		self.app.run(host=host,port=port)