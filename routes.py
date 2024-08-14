from flask import render_template, request
from app import app
from app.search import search_query
import json

try:
    with open('data/index.json', 'r') as f:
        index = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    index = {}

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        results = search_query(query, index)
        return render_template('results.html', query=query, results=results)
    return render_template('index.html')

