
from flask import render_template, request, redirect, Response
from flask import Flask
import random, json

app = Flask(__name__)


@app.route("/")
def main():
<<<<<<< HEAD
    return render_template('profile_page.html')


@app.route('/receiver', methods = ['POST'])
def worker():
    print("POST request")
    print(request.is_json)
    content = request.get_json()
    print(content['device'])
=======
    return render_template('navbar.html')
>>>>>>> 86649cf8478a067dd62b9278dbcc7d22737378fd

#	data = request.get_json()
#    result = ''

    #for item in data:
    #    # loop over every row
    #    result += str(item['device']) + '\n'

    return 'JSON posted'