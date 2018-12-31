'''
URI 요청에 따른 응답에 JSON 데이터를 전달
실제 production에서는 DB와 연동
실습에서는 Dictionary형 데이터를 활용
'''
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    data = {'animal':'rabbit','fruit':'apple'}
    return jsonify(data)

@app.route('/elice_info')
def hello_rabbit(rabbit_num):
    data ={'animal':'white','character':'elice'}
    return jsonify(data)
