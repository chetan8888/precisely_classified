from flask import Flask, render_template, url_for , request,redirect,make_response,session
from flask import send_file
import os
# from main import *

app = Flask(__name__)


# #POST-used to recieve the data
# #GET-used to send the data back 

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/dummyform', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("fname")
       # getting input with name = lname in HTML form 
       last_name = request.form.get("lname") 
       return "Your name is "+first_name + last_name
    return render_template("form.html")

app.run(port=3000) #specify the port for the app tp run
