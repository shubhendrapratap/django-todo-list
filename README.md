# Django To-Do List App

## Overview
This project is a web-based To-Do List application built with Django and Django REST Framework (DRF). The application allows users to create, read, update, and delete tasks. Each task includes details such as a title, description, due date, tags, and status. The project also includes features like basic authentication, unit and integration tests, and CI/CD using GitHub Actions.

## Features
- **Create, Read, Update, Delete (CRUD) Operations**: Manage your tasks with ease.
- **User Authentication**: Secure your endpoints with basic authentication.
- **Django Admin**: Manage tasks through the Django admin interface.
- **REST API**: Access and manage tasks using RESTful endpoints.
- **Unit and Integration Tests**: Ensure code quality with 100% test coverage.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Automated testing and deployment using GitHub Actions.

## Installation

### Prerequisites
- Python 3.11+
- Django 4.2.7+
- Django REST Framework 3.14.0+
- Virtual environment tool (e.g., `venv`)

### Setup
python -m venv myenv
myenv\Scripts\activate  # On Windows
# source myenv/bin/activate  # On macOS/Linux
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


