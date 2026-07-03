# Resume Screener

An AI-powered tool that analyzes how well a resume matches a job description or job title, using NLP and text similarity scoring. Built to simplify and bring transparency to the resume screening process for HR and job seekers alike.

## Features
- Upload resumes in PDF or DOCX format
- Enter either a short job title (e.g. "Full Stack Developer") or a full job description
- Get an instant match score with a clear suitability verdict
- Animated, modern UI with emoji-based feedback
- Fully open-source — no external APIs or paid services required

## Tech Stack
- **Backend:** Python, Flask
- **NLP/ML:** scikit-learn (TF-IDF, cosine similarity)
- **File Parsing:** pdfplumber, python-docx
- **Frontend:** HTML, CSS (custom animations), Font Awesome

## How It Works
1. User uploads a resume and enters a job title or description
2. Short job titles are automatically expanded into relevant skill keywords
3. The app extracts raw text from the resume file
4. Both texts are cleaned and vectorized using TF-IDF
5. Cosine similarity calculates a match percentage
6. A verdict (Strong Match / Moderate Match / Not Suitable) is shown with an emoji reaction

## Setup & Installation

```bash
git clone https://github.com/YOUR_USERNAME/resume-screener.git
cd resume-screener
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## Future Improvements
- Semantic matching using sentence embeddings (catch synonyms like "ML" vs "Machine Learning")
- Skill-gap extraction (highlight specific missing keywords)
- Resume quality checks (formatting, sections, action verbs)

## License
MIT