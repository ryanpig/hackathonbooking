
from flask import render_template, request, redirect, Response
from flask import Flask
import random, json

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('profile_page.html')


@app.route('/receiver', methods = ['POST'])
def worker():
    print("POST request")
    print(request.is_json)
    content = request.get_json()
    print(content['device'])

#	data = request.get_json()
#    result = ''

    #for item in data:
    #    # loop over every row
    #    result += str(item['device']) + '\n'

    return 'JSON posted'