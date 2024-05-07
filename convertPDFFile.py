import PyPDF2

class convertPDFFile:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def convert(self):
        text = ''
        try:
            with open(self.filepath, 'rb') as file:
                pdf = PyPDF2.PdfReader(file)
                for page in pdf.pages:
                    text += page.extract_text() + '\n'
            return True, text
        except Exception as e:
            return False, text
        