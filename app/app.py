from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('home'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('home'))
    
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        
        # Load and clean the data
        data = pd.read_csv(filepath, sep=';', encoding='utf-8', error_bad_lines=False)
        cleaned_data = data.dropna()

        # Perform EDA (as an example, display first few rows)
        eda_result = cleaned_data.head().to_html()

        # Perform prediction (placeholder, replace with actual prediction logic)
        prediction_result = "Prediction results here"
        
        return render_template('home.html', data=eda_result, prediction=prediction_result)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
