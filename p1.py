from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
import hashlib
app = Flask(__name__)
digest = {}

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/messages', methods=['POST'])
def store_message():
	global digest
	message = request.json['message']
	_hash = hashlib.sha256(message)
	d = {}
	hexdigest = _hash.hexdigest()
	d['message'] = hexdigest
	digest[hexdigest] = message 
	return jsonify(d)

@app.route('/messages/<string:message_id>', methods=['GET'])
def show_message(message_id):
	global digest
	if message_id in digest:
		d = {}
		d["message"] = digest[message_id]
		return jsonify(d)
	else:
		abort(404)