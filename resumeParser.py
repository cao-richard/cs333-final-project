from convertPDFFile import convertPDFFile
from extractDetails import extractDetails
class ResumeParser:
    def __init__(self, filePath):
        self.filePath = filePath
        self.skills = []
        self.education = []
        self.name = ''
        self.email = ''
        self.text = ''
    
    def convertPDF(self):
        parser = convertPDFFile(self.filePath)
        result, self.text = parser.convert()
        return result
    
    def getSkills(self):
        extractor = extractDetails(self.text)
        result, self.name = extractor.getName()
        return result
    
    def getName(self):
        extractor = extractDetails(self.text)
        result, self.skills = extractor.getSkills()
        return result
        
    def getEducation(self):
        extractor = extractDetails(self.text)
        result, self.education = extractor.getEducation()
        return result
        
    def getEmail(self):
        extractor = extractDetails(self.text)
        result, self.email = extractor.getEmail()
        return result
        