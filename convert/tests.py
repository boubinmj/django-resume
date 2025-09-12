from django.test import TestCase
from .ingest import PDFIngestor

# Create your tests here.

class PDFIngestorTests(TestCase):
    def test_parse_valid_pdf(self):
        text = PDFIngestor.parse('/home/administrator/Documents/cv_convert/convert/media/test1.pdf')
        self.assertIn("This is a test PDF file.", text)