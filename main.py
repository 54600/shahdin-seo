
import google_search
import rewrite_article
from flask import Flask,jsonify,request
import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import random
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/google_search")
def search():
    q = request.args.get('q')
    
    results=google_search.search_results(q)
    return jsonify(results)
@app.route("/search_paragraph")
def get_paragraphs():
    url = request.args.get('url')
    results=google_search.search_paragraph(url)
    return jsonify(results)
@app.route('/spin')
def spin():
    content = request.args.get('content')
    spincontent=rewrite_article.plagiarism_removal(content)
    r={"spin":spincontent,"orignal":content}
    return jsonify(r)
 
if __name__=="__main__":
    app.run()
    # app.run(debug=True,host="192.168.56.1",port=5000)
    
    #app.run(host="192.168.56.1",port=5000)
