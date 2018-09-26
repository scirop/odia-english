from flask import Flask, render_template
import pickle

dictionary = pickle.load(open("dictionary.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html', translation = dictionary['type'])

if __name__ == '__main__':
	app.run()

