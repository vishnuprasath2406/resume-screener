from flask import Flask, render_template, request
import os
from utils.extractor import extract_text
from utils.scorer import get_match_score, get_verdict

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    job_description = request.form['job_description']

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
    resume_file.save(filepath)

    resume_text = extract_text(filepath)
    score = get_match_score(resume_text, job_description)
    verdict = get_verdict(score)

    return render_template('result.html', score=score, verdict=verdict)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)