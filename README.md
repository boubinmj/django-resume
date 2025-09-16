# Django Resume Viewer

A simple Django app that parses a PDF resume and displays it as a web page in HTML.

## Features
- Extracts text from a PDF resume
- Splits out Resume sections based on keywords
- Splits job experience into bullet points
- Renders section titles, job titles, and supplemtal information.
- Allows user to toggle between viewing HTML and PDF format

## Usage
1. (*OPTIONAL*) Create a virtual environment
    1. Windows
    ```bash
    py -m venv <venv_name>
    <venv_name>\\Scripts\\activate
    2. Unix

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run Server Locally
   ```bash
   python manage.py runserver
4. Visit pages
   ```bash
   http://127.0.0.1:8000/convert/