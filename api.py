import pandas as pd
import joblib
from fastapi import FastAPI
from main import Message

app= FastAPI()

model= joblib.load('spam_model.pkl')
vectorizer= joblib.load('tfidf_vectorizer.pkl')

@app.get('/')
def home():
    return {'message':'Spam Dectection Model API Running'} 

@app.get('/Welcome')
def get_name(name:str):
    return {'Welcome':f'{name}'}

@app.post('/predict')
def predict(data:Message):
    transformed= vectorizer.transform([data.message])
    prediction= model.predict(transformed)

    if prediction[0]==1:
        result= 'Spam'
    else:
        result= 'Ham'
    
    return {'message': data.message, 'prediction':result}