from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html", title="index")
	
@app.route("/contacto")
def contacto():
	return render_template("contacto.html", title="contacto")