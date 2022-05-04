from flask import Flask

app = Flask(__name__)


# #POST-used to recieve the data
# #GET-used to send the data back 

@app.route('/')

def home():
    return "hello,world"

app.run(port=3000) #specify the port for the app tp run
