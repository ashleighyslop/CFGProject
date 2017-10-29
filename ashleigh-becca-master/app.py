from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route("/") #the URL is just a slash
def hello (): #a function that returns hello world
	return render_template("hello.html")

@app.route("/foods", methods=["POST"])
def show_veg_restaurants():

	form_data = request.form
	callAPI = requests.post("https://maps.googleapis.com/maps/api/place/textsearch/json?query=Vegetarian&sensor=true&location=51.50020.1332&type=restaurant&keyword=vegetarian&key=AIzaSyBPGdiypUzDVz2qCsC4IfwVS6uIr3eogFA",
	data={"type": [form_data["diet"]]})
	print form_data["diet"]
	print callAPI.text
	return render_template("foods.html")

if __name__ == '__main__':
	app.run(debug=True)
