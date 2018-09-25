from flask import Flask
import pickle

dictionary = pickle.load(open("dictionary.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def hello_world():
	return dictionary['abbey']

if __name__ == '__main__':
	app.run()

