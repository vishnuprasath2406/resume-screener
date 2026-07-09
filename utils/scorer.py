import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.roles import expand_query


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\b([a-z]+)\d+\b', r'\1', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def skill_coverage_score(expanded_jd, resume_text):
    jd_words = set(clean_text(expanded_jd).split())
    resume_words = set(clean_text(resume_text).split())

    if not jd_words:
        return 0

    matched = jd_words.intersection(resume_words)
    return round((len(matched) / len(jd_words)) * 100, 2)


def score_single_variant(resume_text, expanded_jd):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(expanded_jd)

    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    vectors = vectorizer.fit_transform([resume_clean, jd_clean])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    tfidf_score = similarity * 100

    coverage_score = skill_coverage_score(expanded_jd, resume_text)

    final_score = round((tfidf_score * 0.15) + (coverage_score * 0.85), 2)
    return final_score


def get_match_score(resume_text, job_description):
    expanded_variants = expand_query(job_description)

    # Try every stack variant, keep the best-matching one
    best_score = 0
    for variant in expanded_variants:
        score = score_single_variant(resume_text, variant)
        if score > best_score:
            best_score = score

    return best_score


def get_verdict(score):
    if score >= 70:
        return {"label": "Strong Match", "message": "This resume aligns well with the job requirements.", "level": "good", "emoji": "🎉"}
    elif score >= 45:
        return {"label": "Moderate Match", "message": "This resume partially matches. Consider tailoring it further.", "level": "moderate", "emoji": "🤔"}
    else:
        return {"label": "Not Suitable", "message": "This resume doesn't match well. Try another resume or revise it.", "level": "bad", "emoji": "😞"}