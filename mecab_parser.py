from flask import Flask, session
from konlpy.tag import Mecab
from collections import defaultdict

mecab = Mecab()
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'parser is working'

@app.route('/pos/nouns/<string>')
def parse_nouns(string):
    res_dict = dict()
    res_dict['res'] = mecab.nouns(string)
    return json.dump(res_dict)

@app.route('/pos/morphs/<string>')
def parse_morphs(string):
    res_dict = dict()
    res_dict['res'] = mecab.morphs(string)
    return json.dump(res_dict)

@app.route('/pos/<string>')
def parse_pos(string):
    res_dict = dict()
    res_dict['res'] = mecab.pos(string)
    return json.dump(res_dict)

if __name__ == '__main__':
    app.run(port=8000)
