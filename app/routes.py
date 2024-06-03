from flask import Blueprint, render_template, request
from .models.analysis import analyze_behavior

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    user_data = request.form.to_dict()
    prediction = analyze_behavior(user_data)
    return render_template('index.html', prediction=prediction)
