from resumeParser import ResumeParser

def main():
    resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.docx')
    print(resumeParser.convertPDF())
    print(resumeParser.getName())
    print(resumeParser.getSkills())
    print(resumeParser.getEducation())
    print(resumeParser.getEmail())
    print(resumeParser.skills)
if __name__ == '__main__':
    main()