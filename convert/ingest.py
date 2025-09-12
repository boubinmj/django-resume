import PyPDF2 as pdf2
import re

class PDFIngestor:
    @staticmethod
    def parse(file_path):
        if not file_path.endswith('.pdf'):
            raise ValueError("File is not a PDF")
        
        titles = ['Github',
                  'Google Scholar',
                  'Blog',
                  'Linkedin',
                  'Career Goals',
                  'Skills',
                  'Education',
                  'Professional Experience',
                  "Patents and Publications"]
        
        with open(file_path, 'rb') as file:
            reader = pdf2.PdfReader(file)
            texts = []
            for page in reader.pages:
                txt = page.extract_text()
                if any(title in txt for title in titles):
                    txt += '\n\n'
                texts.append(txt)

        print(texts)
        print(type("\n".join(filter(None, texts))))
        
        return "".join(filter(None, texts))