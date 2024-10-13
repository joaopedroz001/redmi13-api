import os
from flask import Flask
from flask_cors import CORS
from getData import getData

app = Flask(__name__)
CORS(app, resources={r"/data": {"origins": "*"}})

@app.route('/data')
def index():
	return getData()

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 3333))
	app.run(host='0.0.0.0', port=port, debug=True)