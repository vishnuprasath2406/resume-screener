ROLE_SKILLS = {
    "full stack developer": "javascript python react nodejs html css sql mongodb express api git github rest",
    "frontend developer": "javascript react html css typescript redux tailwind figma responsive design ui ux git",
    "backend developer": "python java nodejs express django flask sql mongodb postgresql api rest git docker",
    "data analyst": "python sql excel powerbi tableau pandas numpy data visualization statistics reporting",
    "data scientist": "python machine learning pandas numpy scikit-learn tensorflow pytorch sql statistics deep learning",
    "software engineer": "python java c++ data structures algorithms git github system design api database",
    "python developer": "python flask django rest api sql git github postgresql mongodb oop unit testing",
    "java developer": "java spring boot hibernate sql microservices rest api git maven junit",
    "devops engineer": "docker kubernetes aws jenkins ci cd terraform linux git ansible cloud monitoring",
    "cloud engineer": "aws azure gcp docker kubernetes terraform linux networking security devops iam",
    "mobile developer": "android ios kotlin swift flutter react native java firebase api git",
    "ui ux designer": "figma sketch adobe xd wireframing prototyping user research design systems css",
}


def expand_query(job_description):
    """
    If the input is a short role title, expand it into a fuller skill-based
    description using the ROLE_SKILLS dictionary. Falls back to the original
    text if it's already a detailed description or an unmatched role.
    """
    query = job_description.strip().lower()

    # If it's a known role title, expand it
    if query in ROLE_SKILLS:
        return job_description + " " + ROLE_SKILLS[query]

    # If it's short (likely just a title, not a full description),
    # try to find a partial match
    if len(query.split()) <= 5:
        for role, skills in ROLE_SKILLS.items():
            if role in query or query in role:
                return job_description + " " + skills

    # Otherwise, it's already a detailed description — use as-is
    return job_description