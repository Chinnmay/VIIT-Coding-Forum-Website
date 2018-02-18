from flask import Flask, jsonify, request
import dbconn

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return '<h1>Hello World!</h1>'


@app.route('/test/', methods=['GET'])
def test_route():
	return '<h1>Auto Deploy Working 2nd Time!</h1>'


@app.route('/api/summaries/', methods=['GET'])
def get_summaries_by_domain():
	domain = request.args.get('domain')
	return jsonify(resultset = dbconn.get_summaries_by_domain(domain))


@app.route('/api/details/', methods=['GET'])
def get_full_details():
	ID = request.args.get('ID')
	if ID is None:
		return jsonify(msg="Error Occurred!"), 500
	try:
		ID = int(ID)
		final_json = dbconn.get_full_details(ID)
		if len(list(final_json.keys())):
			return jsonify(dbconn.get_full_details(ID))
		else:
			return jsonify(msg="Not Found"), 404
	except ValueError:
		return jsonify(msg="Error Occurred! Wrong Value of ID"), 500


if __name__ == '__main__':
	app.run(debug=True)
