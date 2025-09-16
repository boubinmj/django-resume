from django.http import HttpResponse
from django.template import loader
from .ingest import PDFIngestor
from django.shortcuts import render
from django.http import FileResponse
from pathlib import Path

def index(request):
    template = loader.get_template('output.html')
    return HttpResponse(template.render())

def output(request):
    template = loader.get_template('output.html')
    return HttpResponse(template.render())

def convert_pdf_to_text(request):
    if request.method == 'GET':
        try:
            text = PDFIngestor.parse('/home/administrator/Documents/cv_convert/convert/media/ResumeSept2025.pdf')
            template = loader.get_template('convert/show.html')
            return render(request, "convert/show.html", {"text": text})
        except Exception as e:
            return render(request, "convert/show.html", {"error": f"{type(e).__name__}: {e}"}, status=400)
        
def resume_pdf(request):
    pdf_path = Path("/home/administrator/Documents/cv_convert/convert/media/ResumeSept2025.pdf")
    return FileResponse(open(pdf_path, "rb"), content_type="application/pdf")