import unittest
from resumeParser import ResumeParser

class integrationTestResumeParser(unittest.TestCase):
    
    #Checks if valid file type and stores the text in resumeParser class
    def testConvertPDFandResumeParserInteraction(self):
        resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.pdf')
        result = resumeParser.convertPDF()
        self.assertGreater(len(resumeParser.text), 0)
        self.assertTrue(result)
        
    #Checks if invalid file type and does not store the text in resumeParser class    
    def testConvertInvalidFileTypeandResumeParserInteraction(self):
        resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.docx')
        result = resumeParser.convertPDF()
        self.assertEqual(len(resumeParser.text), 0)
        self.assertFalse(result)
    
    #Check if there is a name in the file and store it into resumeParser class
    def testGetNameandResumeParserInteraction(self):
        resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.pdf')
        resumeParser.convertPDF()
        result = resumeParser.getName()
        self.assertGreater(len(resumeParser.name), 0)
        self.assertTrue(result)
    
    #Check if there is an email and stores it into resumeParser class
    def testGetEmailandResumeParserInteraction(self):
        resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.pdf')
        resumeParser.convertPDF()
        result = resumeParser.getEmail()
        self.assertEqual(resumeParser.email, 'john.doe@example.com')
        self.assertTrue(result)
    
    #Check if there are skills in the resume and store in resumeParser class
    def testGetSkillsandResumeParserInteraction(self):
        resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.pdf')
        resumeParser.convertPDF()
        result = resumeParser.getSkills()
        self.assertGreater(len(resumeParser.skills), 0)
        self.assertTrue(result)
    
    #Check if there are education in the resume and store in resumeParser Class
    def testGetEducationandResumeParserInteraction(self):
        resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.pdf')
        resumeParser.convertPDF()
        result = resumeParser.getEducation()
        self.assertGreater(len(resumeParser.education), 0)
        self.assertTrue(result)
        
if __name__ == '__main__':
    unittest.main()
        