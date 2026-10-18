# Student Portfolio Website

## Project Description
A five-page student portfolio website built with Python, Django templates, HTML, and CSS.

## Purpose
To display student information, skills, school projects, and contact details.

## Target Users
Students, teachers, and visitors who want to view a portfolio.

## Features
- Home, About Me, Skills, Projects, and Contact pages
- Template inheritance with base.html and {% block %} / {% extends %}
- Reusable navbar and footer loaded with {% include %}
- Navigation links built with {% url %} and named URL patterns
- CSS loaded with {% load static %} and {% static %}
- Responsive layout for smaller screens

## Technologies Used
Python, Django, HTML, CSS, Git, GitHub

## Setup Instructions
1. Clone this repository: `git clone https://github.com/dacpano12/django-student-project.git`
2. Go into the folder: `cd django-student-project`
3. Create a virtual environment: `python -m venv venv`
4. Activate it (Git Bash): `source venv/Scripts/activate`
5. Install requirements: `pip install -r requirements.txt`
6. Run migrations: `python manage.py migrate`
7. Start the server: `python manage.py runserver`
8. Open http://127.0.0.1:8000/

## Challenges and Solutions
- Git Bash did not accept the Windows activate path (`venv\Scripts\activate`). I used `source venv/Scripts/activate` instead.
- A blank page appeared because the template files were empty or misnamed. I fixed the file names and added the content.
- I lost track of which project folder I was in. I located it with `find` and opened it as a folder in VS Code.

## Future Improvements
- A working contact form
- Database-backed projects list
- Photos for each project

## Acknowledgment
I used Claude (Anthropic) as a learning assistant to understand Django, review code examples, and troubleshoot errors. I tested the project myself and can explain how it works.
