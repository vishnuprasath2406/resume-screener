ROLE_SKILLS = {
    "full stack developer": (
        "javascript python react nodejs html css sql mongodb express api "
        "git github rest django flask mysql sqlite bootstrap oop mvc rbac "
        "postgresql typescript rest api development"
    ),
    "frontend developer": (
        "javascript react html css typescript redux tailwind figma "
        "responsive design ui ux git bootstrap vue angular sass webpack"
    ),
    "backend developer": (
        "python java nodejs express django flask sql mongodb postgresql "
        "api rest git docker mysql sqlite oop mvc rbac spring boot microservices"
    ),
    "data analyst": (
        "python sql excel powerbi tableau pandas numpy data visualization "
        "statistics reporting matplotlib seaborn dashboards data cleaning"
    ),
    "data scientist": (
        "python machine learning pandas numpy scikit-learn tensorflow "
        "pytorch sql statistics deep learning nlp data visualization "
        "feature engineering model deployment"
    ),
    "software engineer": (
        "python java c++ data structures algorithms git github system "
        "design api database oop django flask rest sql mysql testing"
    ),
    "python developer": (
        "python flask django rest api sql git github postgresql mongodb "
        "oop unit testing mysql sqlite mvc rbac api development pytest"
    ),
    "java developer": (
        "java spring boot hibernate sql microservices rest api git maven "
        "junit oop mvc mysql postgresql"
    ),
    "devops engineer": (
        "docker kubernetes aws jenkins ci cd terraform linux git ansible "
        "cloud monitoring azure gcp bash scripting infrastructure automation"
    ),
    "cloud engineer": (
        "aws azure gcp docker kubernetes terraform linux networking "
        "security devops iam cloud architecture load balancing monitoring"
    ),
    "mobile developer": (
        "android ios kotlin swift flutter react native java firebase "
        "api git mobile ui design sqlite rest api"
    ),
    "ui ux designer": (
        "figma sketch adobe xd wireframing prototyping user research "
        "design systems css responsive design accessibility usability testing"
    ),
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