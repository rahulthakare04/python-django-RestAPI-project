



# Django REST API Project

This project contains a Django-based REST API for handling various functionalities, including students, books, and football players.

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install django
```

## API Endpoints

### Students API

- **Get All Students** (`GET /students/all/`)
- **Add Student** (`POST /student/add/`) *(Pending Implementation)*
- **Update Student Age** (`POST /student/ageupdate`) *(Pending Implementation)*
- **Delete Student** (`POST /student/delete`) *(Pending Implementation)*

### Books API

- **Get All Books** (`GET /books/all/`)

### Football Players API

- **Get Players by Nationality** (`POST /player/nation/` with `nation` in the request body)

## Running the API

1. Navigate to the project directory and run migrations:

```bash
python manage.py migrate
```

2. Start the Django server:

```bash
python manage.py runserver
```

## Video Execution

[For a step-by-step guide on setting up and running the Django REST API project, refer to the provided video tutorial.](https://github.com/user-attachments/assets/723596ea-0f91-4711-beca-ba8befbec46c)

## Notes

- The API connects to MySQL and MongoDB databases.
- Ensure the database credentials are correctly configured in the Django settings.
- Run the server in a Python environment with the necessary dependencies installed.

