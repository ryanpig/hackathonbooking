
from flask import render_template, request, redirect, Response
from flask import Flask
import random, json

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('profile_page.html')


@app.route('/no', methods = ['post'])
def handle_data():
    print("POST request")
    print(request.form)
#     print(request.is_json)
#     content = request.get_json()
#     print(content['device'])
#     return render_template('navbar.html')