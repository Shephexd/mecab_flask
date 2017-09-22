from flask import Flask
from konlpy.tag import Mecab
from collections import defaultdict

mecab = Mecab()
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'parser is working'

@app.route('/pos/nouns/<string>', methods=['GET', 'POST'])
def parse_nouns(string):
    mecab.nouns(string)

@app.route('/pos/morphs/<string>', method=['GET', 'POST'])
def pasrse_morphs(string):
    mecab.morphs(string)

@app.route('/pos/<string>', method=['GET', 'POST'])
def pasrse_morphs(string):
    mecab.pos(string)

if __name__ == '__main__':
    app.run(port=8000)
