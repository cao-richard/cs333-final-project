import spacy
from spacy.matcher import Matcher
import csv

nlp = spacy.load('en_core_web_sm')

class extractDetails:
    def __init__(self, text):
        self.text = text
        self.skills_file_path = 'skills.csv'
        self.skills = []
        
    def getName(self):
        name = ''
        doc = nlp(self.text)
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                name = ent.text
                return True, name
        return False, name
    
    def getEmail(self):
        email = ''
        doc = nlp(self.text)
        for token in doc:
            if token.like_email:
                email = token.text
                return True, email
        return False, email
    
    def loadSkills(self):
        skills_list = []
        with open(self.skills_file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                skills_list.extend(row)
        self.skills = skills_list
        
    def getSkills(self):
        self.loadSkills()
        resumeSkills = []
        for skill in self.skills:
            if skill in self.text and skill not in resumeSkills:
                resumeSkills.append(skill)
        if resumeSkills == []:
            return False, resumeSkills
        else:
            return True, resumeSkills
        
    def getEducation(self):
        schools = ['university', 'college']
        doc = nlp(self.text.lower())
        education = []
        for ent in doc.ents:
            if ent.label_ == "ORG" and any(school in ent.text for school in schools):
                education.append(ent.text)
        if education == []:
            return False, education
        else:
            return True, education