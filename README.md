# Smart Notes Application

A Django-based web application for creating, managing, and sharing smart notes. Built by following LinkedIn Learning's [Django Essential Training](https://www.linkedin.com/learning/django-essential-training-25094632).

## Features
- User authentication (register, login, logout)
- Public and private notes
  - Public notes are accessible to all users
  - Private notes are visible only to their creators
- Create, view, update, and delete notes
- Like notes (social feature)
- Responsive UI with custom CSS
- Access control for authorized pages

## Project Structure
- `home/`: Handles user authentication, registration, and home views
- `notes/`: Manages note CRUD operations, likes, and note visibility
- `smartnotes/`: Project configuration and URL routing
- `static/`: CSS and static assets
- `templates/`: HTML templates for all pages

## Getting Started

### Prerequisites
- Python 3.13+
- Django 5.2+

### Setup
1. Clone the repository
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv django_venv
   source django_venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install django
   ```
4. Run migrations:
   ```sh
   python manage.py migrate
   ```
5. Start the development server:
   ```sh
   python manage.py runserver
   ```
6. Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage
- Register a new account or log in
- Create, edit, or delete your notes
- Set notes as public or private
- Like public notes
- Log out securely (POST request required)

## Folder Overview
- `home/` - User authentication and home views
- `notes/` - Note models, views, forms, and templates
- `smartnotes/` - Project settings and URLs
- `static/` - CSS styles
- `templates/` - Base and app-specific HTML templates

## License
This project is for educational purposes.
