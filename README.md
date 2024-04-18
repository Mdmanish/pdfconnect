# Django PDF Processing

This Django web application allows users to upload PDF files, ask question and api will be give the answer based on uploaded pdf data.

## Getting Started

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-pdf-processing.git
```
### 2. Install Dependencies
Navigate to the project directory and install project dependencies using pip:

```bash
cd /path/to/project
pip install -r requirements.txt
create an account and api key from this link https://api.chatpdf.com/
Replace YOU_API_KEY with your create api key inside pdfcoonect/pdfhub/utils.py file
```
### 4. Apply Migrations
Apply migrations to create the database schema:
```
python manage.py makemigrations
python manage.py migrate
```
### 5. Run the Development Server
Run the Django development server:
```
python manage.py runserver
```
Access the application in your web browser at http://localhost:8000.

Usaer Register (http://localhost:8000/register/): Create a new user account with details and upload PDF files.
Login (http://localhost:8000/login): Access your account to view uploaded PDFs and ask questions.
