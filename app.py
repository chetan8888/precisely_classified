from flask import Flask, render_template

app = Flask(__name__)


# #POST-used to recieve the data
# #GET-used to send the data back

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/form')
def form():
    return render_template("form.html")


app.run(port=3000)  # specify the port for the app tp run
