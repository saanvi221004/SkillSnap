# app.py
from flask import Flask, render_template, request
import os
from utils.resume_parser import extract_skills
import pickle

app = Flask(__name__)
model = pickle.load(open('models/model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    skills = []
    if request.method == 'POST':
        resume_text = request.form['resume']
        skills = extract_skills(resume_text)
        input_skills = " ".join(skills)
        prediction = model.predict([input_skills])[0]
    return render_template('index.html', prediction=prediction, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
