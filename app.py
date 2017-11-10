from flask import Flask, render_template, request, session, redirect, url_for
import json, urllib2

app = Flask(__name__)

@app.route("/")
def nAssa():
	
	#Make and parse a REST call in python
	url = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=dmWuXHula8sV8Y2uSJXhfjW2X8J6n84MCzchQrYk")
	dic = json.loads(url.read())
	
	return render_template("base.html", title = dic["title"], image = dic["hdurl"], date = dic["date"], explanation = dic["explanation"])

if __name__ == "__main__":
	app.debug = True
	app.run()