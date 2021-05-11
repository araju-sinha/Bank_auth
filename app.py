#importing important libraries
from flask import Flask,request 
import pandas as pd
import numpy as np
import pickle

#Main execution line to run app
app = Flask(__name__)

#import the model/classifier
pickle_in = open("Classifier.pkl","rb")
classifier  = pickle.load(pickle_in)

#dacurater for root path
@app.route('/')
#create a function for homepage
def welcome():
    return "Welcome all"

#dacurater for prediction path
@app.route('/predict')
#create a function to take variables and thn predict the result using classifier 
def predict_note():
    variance  = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy  = request.args.get("entropy")
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is " + str(prediction)

#dacurater for prediction_file path
@app.route('/predict_file',methods=['POST'])
#create a function to take variables from file and thn predict the result using classifier 
def predict_note_file():
    df_test = pd.read_csv("file")
    prediction  = classifier.predict(df_test)
    return "The predicted value is " + str(list(prediction))

#whenever __name__ = __main__ the app will run
if __name__ == '__main__':
    app.run()
    