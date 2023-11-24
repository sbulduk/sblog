from flask import Flask

def configure_routes(app:Flask):
	@app.route("/users")
	def users():
		return "The users page"