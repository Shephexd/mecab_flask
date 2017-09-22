from flask import Flask, session, request
from konlpy.tag import Mecab
from collections import defaultdict
import json

mecab = Mecab()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'parser is working'

@app.route('/pos/nouns/', methods=['POST'])
def parse_nouns():
    res_dict = dict()
    string = request.form['text']
    res_dict['res'] = mecab.nouns(string)
    return json.dumps(res_dict)

@app.route('/pos/morphs/', methods=['POST'])
def parse_morphs():
    res_dict = dict()
    string = request.form['text']
    res_dict['res'] = mecab.morphs(string)
    return json.dumps(res_dict)

@app.route('/pos/', methods=['POST'])
def parse_pos():
    res_dict = dict()
    string = request.form['text']
    res_dict['res'] = mecab.pos(string)
    return json.dumps(res_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
