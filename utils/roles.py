ROLE_SKILLS = {
    "full stack developer": [
        "javascript react nodejs html css mongodb express typescript git github rest api",
        "python django mysql sqlite bootstrap html css git github rest api oop mvc rbac"
    ],
    "frontend developer": [
        "javascript react html css typescript redux tailwind figma responsive design ui ux git bootstrap vue angular sass webpack"
    ],
    "backend developer": [
        "python django flask mysql sqlite api rest git oop mvc rbac postgresql",
        "java spring boot hibernate sql microservices rest api git maven",
        "nodejs express mongodb rest api git"
    ],
    "data analyst": [
        "python sql excel powerbi tableau pandas numpy data visualization statistics reporting matplotlib seaborn dashboards data cleaning"
    ],
    "data scientist": [
        "python machine learning pandas numpy scikit-learn tensorflow pytorch sql statistics deep learning nlp data visualization feature engineering model deployment"
    ],
    "software engineer": [
        "python java c++ data structures algorithms git github system design api database oop testing"
    ],
    "python developer": [
        "python flask django rest api sql git github postgresql mongodb oop unit testing mysql sqlite mvc rbac pytest"
    ],
    "java developer": [
        "java spring boot hibernate sql microservices rest api git maven junit oop mvc mysql postgresql"
    ],
    "devops engineer": [
        "docker kubernetes aws jenkins ci cd terraform linux git ansible cloud monitoring azure gcp bash scripting infrastructure automation"
    ],
    "cloud engineer": [
        "aws azure gcp docker kubernetes terraform linux networking security devops iam cloud architecture load balancing monitoring"
    ],
    "mobile developer": [
        "android ios kotlin swift flutter react native java firebase api git mobile ui design sqlite rest api"
    ],
    "ui ux designer": [
        "figma sketch adobe xd wireframing prototyping user research design systems css responsive design accessibility usability testing"
    ],
}


def expand_query(job_description):
    """
    Returns a LIST of possible expansions for the role (different tech stacks),
    or a single-item list with the original text if no match is found.
    """
    query = job_description.strip().lower()

    if query in ROLE_SKILLS:
        return [job_description + " " + variant for variant in ROLE_SKILLS[query]]

    if len(query.split()) <= 5:
        for role, variants in ROLE_SKILLS.items():
            if role in query or query in role:
                return [job_description + " " + variant for variant in variants]

    return [job_description]