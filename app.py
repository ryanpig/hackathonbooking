
from flask import render_template, request, redirect, Response
from flask import Flask
import random, json
from random import choice

#from testjson import writejson, readjson
from user_match import match_process
import urllib
def readjson():
    with open('profile_1.txt', 'r') as outfile:
        data = json.load(outfile)
    return data
def writejson(data):
    with open('profile_1.txt', 'w') as outfile:
        json.dump(data, outfile)


app = Flask(__name__)
count = 0


@app.route("/")
def main():
    return render_template('confirmation.html')

@app.route("/profile_page.html")
def user_profile():
	return render_template("profile_page.html")


@app.route('/no', methods = ['post'])
def handle_data():
    print("POST request")
    v1 = request.form['usr_first']
    v2 = request.form['usr_home']
    v3 = request.form.getlist('lang')
    print(request.form.getlist('lang'))
    t = {
        "usr_first": v1,
        "usr_home" : v2,
        "lang" : v3
    }
    writejson(t)
    #usr_name, usr_langs = match_process()
    #print(request.form['usr_first'])
    #print(request.form['usr_home'])
    #print(usr_name)
    #print(usr_langs)
    return render_template('journey_detail.html')

@app.route('/no2', methods = ['post'])
def render_user_matching():
    user_dict1 = {"Name": "Julian",
                  "Gender": "Male",
                  "Country": "GB",
                  "Languages": "Spanish, English",
                  "Hotel": "Cool Hotel",
                  "Dates": "29.04-01.05",
                  "Travel_Description": "ok",
                  "IMG": "https://vecer.mk/files/article/2016/02/29/357398-mazhite-koi-pochesto-imaat-seks-se-popametni.png"}
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

    user_list_end = '''		
    			</div>
    		<div class="col-md-4">
    			<div class="row">
    				<div class="well well-lg" style="padding: 5">
    					<div class="row">
    						<div class="col-md-1">
    						</div>
    						<div class="col-md-10" id="chat">
    						</div>
    					</div>

    					<form>
    					  	<svg width="400" height="170" id="svg">
    						  	<rect width="100%" height="100%" style="fill:None;stroke-width:0;stroke:None" />
    						</svg>
    					  	<div class="form-group">
    					    <label for="exampleFormControlTextarea1"></label>
    					    	<textarea class="form-control" rows="3" id="textarea"></textarea>
    					  	</div>
    					</form>
    				</div>
    			</div>
    			<script>
    				var input = document.getElementById("textarea")
    				input.addEventListener("keyup", function(event) {
    			  // Cancel the default action, if needed
    			  event.preventDefault();
    			  // Number 13 is the "Enter" key on the keyboard
    			  if (event.keyCode === 13) {
    			    // Trigger the button element with a click
    			    console.log("ok")
    			    var message = document.getElementById("textarea").value
    			    input.value = ""
    			    send_message(message)
    			  }
    			});
    			</script>'''
    groups = '''
    			<div class="row">
    				<div class="well">

    					{0}, {1}, {2} is joining.<br>
    					<div class="row">
    				<div class="col-md-12">
    					<button type="button submit" class="btn btn-primary btn-block" onclick="location.href='/render_group.html'">Join</button>
    				</div>
    			</div>
    				</div>
    			</div>'''
    groups_tail = '''
    		</div>
    	</div>
    </div>
    '''

    # generate matching profiles
    usr_name, usr_langs, usr_gender, usr_stay = match_process()
    user_dicts = []

    for x in range(len(usr_name)):
        WORDS = []
        with open("words.txt") as f:
            for row in f:
                WORDS.append(row.split(",")[0])
        hotelname = str(choice(WORDS))[:-1].title()
        hotelname += " Hotel"

        user_dict1['Name'] = usr_name[x]
        user_dict1['Languages'] = usr_langs[x]
        user_dict1['Gender'] = usr_gender[x]
        user_dict1['Dates'] = usr_stay[x]
        user_dict1['Hotel'] = hotelname
        if usr_gender[x] == 'Female':
            user_dict1['IMG'] = "https://media.gettyimages.com/photos/portrait-of-a-beautiful-young-student-girl-in-the-park-picture-id507838794?b=1&k=6&m=507838794&s=612x612&w=0&h=PyK_awvtorTGdgRHCAC8LI7Jg3wzHOGGiNdYXf-IGDg="
        else:
            user_dict1['IMG'] = "https://vecer.mk/files/article/2016/02/29/357398-mazhite-koi-pochesto-imaat-seks-se-popametni.png"

        user_dicts.append(user_dict1)
        output_html += user_specific.format(**user_dicts[x])


    output_html += user_list_end
    group_names = ["Foodies", "Sightseeing", "Beach4Life","Group4", "Group5"]

    for x in range(len(usr_name)):
        #output_html += groups.format(group_names[0], user_dicts[x]["Dates"], user_dicts[x]["Name"])
        output_html += groups.format(group_names[x], user_dicts[x]["Dates"], user_dicts[x]["Name"])

    output_html += groups_tail

    #output_html += final_url
    return output_html


@app.route('/render_group.html')
def group():
    return render_group()

@app.route('/group', methods=['post'])
def render_group():
    output_html = '''
	<head>
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
		<div class="row">
			<div class="col-md-1"
			</div>
			</div class="col-md-4">
			<b>Foodies (29.04-01.05)</>
			</div>
		</div>
		<div class="col-md-2">
			<div class="row">
					<button type="button" class="btn btn-primary btn-block"> Day 1</button>
			</div>
			<div class="row">
				<button type="button" class="btn btn-primary btn-block"> Day 2</button>
			</div>
			<div class="row">
				<button type="button" class="btn btn-primary btn-block"> Day 3</button>
			</div>
		</div>
		<div class="col-md-5">
		<img src="static/rec.png" width="600">
		</div>
		<div class="col-md-5">
			<div class="row">
				<div class="well well-lg" style="padding: 5">
					<div class="row">
						<div class="col-md-1">
						</div>
						<div class="col-md-10" id="chat">
						</div>
					</div>

					<form>
					  	<svg width="400" height="170" id="svg">
						  	<rect width="100%" height="100%" style="fill:None;stroke-width:0;stroke:None" />
						</svg>
					  	<div class="form-group">
					    <label for="exampleFormControlTextarea1">Chat with Foodies</label>
					    	<textarea class="form-control" rows="3" id="textarea"></textarea>
					  	</div>
					</form>
				</div>
			</div>
			<img src="https://s3.eu-west-2.amazonaws.com/troopscout/deals/hertz-car-rental-military-armed-20-discount.jpg" width="400">
		</div>


	'''
    return output_html



