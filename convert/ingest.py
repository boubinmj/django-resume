import PyPDF2 as pdf2
import re

class PDFIngestor:
    @staticmethod
    def parse(file_path):
        if not file_path.endswith('.pdf'):
            raise ValueError("File is not a PDF")
        
        titles = ['Experience',
                  'Education',
                  'Publications']
        
        with open(file_path, 'rb') as file:
            reader = pdf2.PdfReader(file)
            texts = []
            for page in reader.pages:
                txt = page.extract_text().strip('\n')
                txt = txt.replace('\n', ' ')
                if any(title in txt for title in titles):
                    txt += '\n\n'
                texts.append(txt)
        
        pattern = r"(" + "|".join(map(re.escape,titles)) + r")"
        print(pattern)
        try:
            lst = re.split(pattern, texts[0])
        except Exception as e:
            print(f"Error during regex split: {e}")

        for el in lst:
            print(el)
            print("-----")
        #print(type("".join(filter(None, texts))))
        
        return "".join(filter(None, texts))