from resumeParser import ResumeParser

def main():
    path = input('Path to your resume in a PDF format ')
    resumeParser = ResumeParser(path)
    resumeParser.convertPDF()
    resumeParser.getName()
    resumeParser.getSkills()
    resumeParser.getEducation()
    resumeParser.getEmail()
    print('Name: ' + resumeParser.name)
    print('Email: ' + resumeParser.email)
    print('Skills: ' + ', '.join(resumeParser.skills))
    print('Location of education: ' + ', '.join(resumeParser.education))
if __name__ == '__main__':
    main()