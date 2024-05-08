import unittest
from resumeParser import ResumeParser
from convertPDFFile import convertPDFFile
from extractDetails import extractDetails

class TestPDFConverter(unittest.TestCase):
    def test_ActualPDFFile(self):
        resumeParser = convertPDFFile('Computer_Science_Resume_John_Doe.pdf')
        result, text = resumeParser.convert()
        self.assertTrue(result)
    
    def test_NotPDFFile(self):
        resumeParser = convertPDFFile('Computer_Science_Resume_John_Doe.docx')
        result, text = resumeParser.convert()
        self.assertFalse(result)

class TestExtractDetails(unittest.TestCase):
    def setUp(self):
        converter = convertPDFFile('Computer_Science_Resume_John_Doe.pdf')
        result, self.text = converter.convert()
    
    def test_GetName(self):
        extraction = extractDetails(self.text)
        result, name = extraction.getName()
        self.assertTrue(result)
    
    def test_getSkills(self):
        extraction = extractDetails(self.text)
        result, skills = extraction.getSkills()
        self.assertTrue(result)
        
    def test_getEducation(self):
        extraction = extractDetails(self.text)
        result, education = extraction.getEducation()
        self.assertTrue(result)
    
    def test_getEmail(self):
        extraction = extractDetails(self.text)
        result, email = extraction.getEmail()
        self.assertTrue(result)

class TestResumeParser(unittest.TestCase):
    def setUp(self):
        self.resumeParser = ResumeParser('Computer_Science_Resume_John_Doe.pdf')
    
    def test_convertPDF(self):
        result = self.resumeParser.convertPDF()
        self.assertTrue(result)
    
    def test_getName(self):
        result = self.resumeParser.getName()
        self.assertTrue(result)
        
    def test_getEmail(self):
        result = self.resumeParser.getEmail()
        self.assertTrue(result)
        
    def test_getSKills(self):
        result = self.resumeParser.getSkills()
        self.assertTrue(result)
        
    def test_getEducation(self):
        result = self.resumeParser.getEducation()
        self.assertTrue(result)