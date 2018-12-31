from flask import Flask
app = Flask (__name__)

@app.route('/')
def hello_world()
    return 'Hello, World!'

@app.route('/rabbit/<rabbitname>')
def hello_rabbit(rabiitname):
    return 'Hello,'+rabbitname+'!'
