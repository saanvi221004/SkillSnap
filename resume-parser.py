# utils/resume_parser.py
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    skills = ["Python", "Java", "SQL", "HTML", "CSS", "Flask", "Machine Learning", "Communication", "Leadership"]
    doc = nlp(text)
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    return list(set(found_skills))
