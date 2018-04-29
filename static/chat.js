var replies_sent = 0
var chat_height = 20

function start_chat(user_name) {
	document.getElementById("chat").innerHTML = "You are chatting with " + "<b>"+ user_name+"</b>"
	document.getElementById("svg").innerHTML = ''
	replies_sent = 0
	chat_height = 20
}


function send_reply() {
	if (replies_sent == 0) {
		var message = "Hey there! :)"
	} else if (replies_sent == 1) {
		var message = "Yes, sounds fun!"
	} else {
		var message = "Sounds great!"
	}
	document.getElementById("svg").innerHTML += '<text y="' + chat_height+ '" x="200" font-size="16px" fill="black">' + message+ '</text>'
	chat_height = chat_height + 30
	replies_sent = replies_sent += 1


}


function send_message(message) {
	console.log("message")
	document.getElementById("svg").innerHTML += '<text y="' + chat_height+ '" x="20" font-size="16px" fill="black">' + message + '</text>'
	chat_height = chat_height + 30
	window.setTimeout(send_reply, 3000)

}

