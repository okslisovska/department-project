import requests
from flask import request, url_for
from app import app


@app.route('/')
def index():
    return "<h1>Department-project</h1><p>will be here soon</p>"


@app.route('/departments')
def departments():
    api_url = request.host_url[:-1] + url_for('api.get_departments')
    response = requests.get(api_url)
    return response.text
