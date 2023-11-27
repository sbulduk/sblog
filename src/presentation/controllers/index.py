from flask import Flask

def configure_routes(app:Flask):
	@app.route("/")
	def index():
		return "The index page"
	
	@app.route("/<string:address>")
	def address(address):
		return f"Dynamic address {address}"