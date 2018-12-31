from flask import Flask

app = Flask (__name__)
@app.route('/')
def hello_world():
    return 'Hello,World!'
    
@app.route('/rabbit/<int:rabbitname>')
def hello_rabbit(rabbit_num):
    return 'Hello,%d!'%rabbit_num
