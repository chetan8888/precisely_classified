from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


# #POST-used to recieve the data
# #GET-used to send the data back

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/handle_data', methods=['POST'])
def handle_data():
    print("Dataframe format required for Machine Learning prediction")
    df = pd.DataFrame([request.form.values()], columns=request.form.keys())
    print(df)
    # print("tell", request.form.to_dict())
    # form_data = request.form["job"]
    # form_data1 = request.form["education"]
    # form_data2 = request.form["age"]
    # form_data3 = request.form["balance"]
    # form_data4 = request.form["default"]
    # form_data5 = request.form["housing"]
    # form_data6 = request.form["loan"]
    # print("form data", form_data)
    # print("form data1", form_data1)
    # print("form data2", form_data2)
    # print("form data3", form_data3)
    # print("form data4", form_data4)
    # print("form data5", form_data5)
    # print("form data6", form_data6)
    return
    # your code
    # return a response


app.run(port=3000)  # specify the port for the app tp run
