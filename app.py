from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	# Alternative Usage of Saved Model
	#joblib.dump(clf, 'NB_spam_model.pkl')
	NB_spam_model = open('NB_spam_modelsvm.pkl','rb')
	NB_spam_model1 = open ( 'NB_spam_model1svm.pkl', 'rb' )
	cf = joblib.load(NB_spam_model)
	cv1 = joblib.load ( NB_spam_model1 )

	if request.method == 'POST':
		message = request.form['message']
		data = [message]
		vect = cv1.transform(data).toarray()
		my_prediction = cf.predict(vect)
	return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)
