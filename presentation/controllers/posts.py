from flask import Flask,request
import json

def configure_routes(app:Flask):
	data_path="temp_data/posts.json"
	with open(data_path,"r") as f:
		list=json.load(f)
	
	@app.route("/posts",methods=["GET","POST"])
	def posts():
		if(request.method=="GET"):
			if(len(list)>0):
				return list
			else:
				return "No books found!"
		if(request.method=="POST"):
			new_data={
				"id":4,
				"author":"Test Author",
				"language":"Test Language",
				"title":"Test Title",
			}
			list.append(new_data)
			with open(data_path,"w"):
				json.dump(list,f)
			print("Data added successfully!")

	@app.route("/books/<int:id>",methods=["GET"])
	def get_by_id(id:int):
		for book in list:
			if(book["id"]==id):
				return book
		print("No Book!!!")