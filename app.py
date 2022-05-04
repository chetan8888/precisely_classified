from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# #POST-used to recieve the data
# #GET-used to send the data back 

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/post_form', methods=['GET','POST'])
def post_form():
    if request.method == 'POST':
        # Call the ML model here
        cust_name = request.form['cust_name']
        return render_template('result.html', cust_name=cust_name)
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True) #specify the port for the app tp run
