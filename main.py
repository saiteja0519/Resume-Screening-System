from resume_parser import extract_text
from skill_matcher import match_skills
from ranking import save_candidate, display_ranking
import os

REQUIRED_SKILLS = ["python", "sql", "data structures", "machine learning"]

def main():
    resume_folder = "sample_resumes"

    for file in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, file)
        text = extract_text(file_path)

        score = match_skills(text, REQUIRED_SKILLS)
        candidate_name = file.replace(".txt", "")

        save_candidate(candidate_name, score)

    display_ranking()

if __name__ == "__main__":
    main()
