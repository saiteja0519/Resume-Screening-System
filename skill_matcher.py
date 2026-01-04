def match_skills(resume_text, required_skills):
    score = 0
    for skill in required_skills:
        if skill.lower() in resume_text:
            score += 1
    return score
