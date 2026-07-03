import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.roles import expand_query


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_match_score(resume_text, job_description):
    job_description = expand_query(job_description)

    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(job_description)

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_clean, jd_clean])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    score = round(similarity * 100, 2)

    return score


def get_verdict(score):
    if score >= 35:
        return {"label": "Strong Match", "message": "This resume aligns well with the job requirements.", "level": "good", "emoji": "🎉"}
    elif score >= 18:
        return {"label": "Moderate Match", "message": "This resume partially matches. Consider tailoring it further.", "level": "moderate", "emoji": "🤔"}
    else:
        return {"label": "Not Suitable", "message": "This resume doesn't match well. Try another resume or revise it.", "level": "bad", "emoji": "😞"}