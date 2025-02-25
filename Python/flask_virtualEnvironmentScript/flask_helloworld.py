import sys
from flask import Flask, jsonify, request 

app = Flask(__name__) 


@app.route('/hello', methods=['GET']) 
def helloworld():
    return f"Hello, World! Running on Python from {sys.executable}"

if __name__ == '__main__': 
	app.run(debug=True) 
