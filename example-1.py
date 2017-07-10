#!/usr/bin/env python

from flask import Flask, jsonify, make_response, render_template, request

##############################################################################
app = Flask(__name__)
app.secret_key = 's3cr3t'

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Niestety nic nie znalalem'}), 404)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/ex1', methods=['GET'])
def getwebmaininfo():
	return render_template('index.html', message='''Hello ! \n
													This is EXAMPLE web page ver. 1.0  '''
	                       )

@app.route('/ex1/api/version', methods=['GET'])
def getapimaininfo():
	return jsonify({
		               'message': '''Hello ! This is EXAMPLE API ver. 1.0 '''})



##############################################################################
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=5000)