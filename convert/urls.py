from django.urls import path
from . import views

app_name = "convert" 

urlpatterns = [
    path("", views.convert_pdf_to_text, name="index"),
    path("output/", views.output, name="output"),
    path("convert-pdf/", views.convert_pdf_to_text, name="convert_pdf_to_text"),
    path("resume-pdf/", views.resume_pdf, name="resume_pdf"),
]