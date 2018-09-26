from flask import Flask, render_template, request
import pickle

e2odictionary = pickle.load(open("dictionary.pkl","rb"))

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/receiver',methods=['POST'])
def translator():
	data = request.get_json()
	words = data.split(" ")
	tr_words = []
	for word in words:
		if word in e2odictionary:
			tr_words.append(e2odictionary[word])
		else:
			tr_words.append("**")
	result = " ".join(tr_words)
	return result


if __name__ == '__main__':
	app.run()

