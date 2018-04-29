
from flask import render_template, request, redirect, Response, Markup
from flask import Flask
import random, json

app = Flask(__name__)


@app.route("/")
def main():
    # return render_template('confirmation.html')
    # return 
	# flash(message)
    return render_template("user_matching.html")
    # return render_user_matching()
@app.route("/profile_page.html")
def user_profile():
	return render_template("profile_page.html")

# @app.route("")

@app.route('/no', methods = ['post'])
def handle_data():
    print("POST request")
    print(request.form)
#     print(request.is_json)
#     content = request.get_json()
#     print(content['device'])
#     return render_template('navbar.html')

def render_user_matching():
	user_dict1 = {"Name": "Julian", 
	"Gender": "Male", 
	"Country": "GB", 
	"Languages": "Spanish, English", 
	"Hotel": "Cool Hotel", 
	"Dates": "29.04-01.05", 
	"Travel_Description": "ok", 
	"IMG": "https://vecer.mk/files/article/2016/02/29/357398-mazhite-koi-pochesto-imaat-seks-se-popametni.png"}
	user_dicts = [user_dict1, user_dict1, user_dict1]

	output_html = '''
	<head>
	<script src="static/chat.js" crossorigin="anonymous"></script>

	<link rel="stylesheet" media="screen" href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
	<script src="https://code.jquery.com/jquery-3.3.1.min.js" crossorigin="anonymous"></script>
	<script src="https://maxcdn.bootstr
	apcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
	<meta name="viewport" content = "width=device-width, initial-scale=1.0">
	</head>
	<nav class="navbar navbar-default" role="navigation">
	  <div class="container-fluid bg-primary">
	    <!-- Brand and toggle get grouped for better mobile display -->
	    <div class="navbar-header ">
	      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
	        <span class="sr-only">Toggle navigation</span>
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>
	        <span class="icon-bar"></span>
	      </button>
	      <a class="navbar-brand" href="#"><img src="https://s-ec.bstatic.com/static/img/b26logo/booking_logo_retina/22615963add19ac6b6d715a97c8d477e8b95b7ea.png" width="150"/></a>
	      </div>
	</div>
	</nav>
	<div class="container">
			<div class="row">
				<div class="col-md-8">
	'''


	user_specific = '''
		<div class="well well-lg" style="padding: 5">
			<div class="row">
				<div class="col-md-4">
					<img src="{IMG}" width="200">
				</div>
				<div class="col-md-8">
					<span style="font-size:16">Name:</span>
					<span style="font-weight:bold; font-size: 16">{Name}</span><br>
					<span style="font-size:16">Gender:</span>
					<span style="font-weight: bold; font-size: 16">{Gender}</span><br>
					<span style="font-size:16">Country:</span>
					<span style="font-weight:bold; font-size: 16">{Country}</span><br>
					<span style="font-size:16">Languages:</span>
					<span style="font-weight:bold; font-size: 16">{Languages}</span><br>
					<span style="font-size:16">Staying at:</span>
					<span style="font-weight:bold; font-size: 16">{Hotel}</span><br>
					<span style="font-size:16">Travel dates:</span>
					<span style="font-weight:bold; font-size: 16">{Dates}</span><br>
					<span style="font-size:16">Trip description:</span>
					<span style="font-weight:bold; font-size: 16">{Travel_Description}</span><br>
				</div>
			</div>
			<div class="row">
				<div class="col-md-4">
				</div>
				<div class="col-md-8">
					<button type="button" class="btn btn-primary btn-block" onclick="start_chat('{Name}')">Message {Name}</button>
				</div>
			</div>
		</div>
	'''

	user_list_end ='''		
			</div>
			<div class="col-md-4">
				<div class="well well-lg">
					<div class="row" id="chat">
					ok
					</div>
				</div>
			</div	
		</div>
	</div>'''
	for x in range(len(user_dicts)):
		output_html += user_specific.format(**user_dicts[x])
	output_html += user_list_end
	return output_html