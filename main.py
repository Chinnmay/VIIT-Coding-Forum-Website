from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return '<h1>Hello World!</h1>'

@app.route('/test', methods=['GET'])
def test_route():
	return '<h1>Auto Deploy Working!</h1>'

if __name__=='__main__':
	app.run()