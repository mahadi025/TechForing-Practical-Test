# Project Management System

This is a Django-based project management system with support for users, projects, tasks, and comments.

## Requirements

- Python 3.12+
- pip
- (Recommended) Virtualenv

## Setup Instructions

1. **Clone the repository**

   ```sh
   git clone <https://github.com/mahadi025/TechForing-Practical-Test.git>
   cd <TechForing-Practical-Test>
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (admin account)**

   ```sh
   python manage.py createsuperuser # A super is already created username:admin, password:admin
   ```

6. **Run the development server**

   ```sh
   python manage.py runserver
   ```

7. **Access the application**

   - Open your browser and go to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure

- `user/` - User management app
- `project/` - Project management app
- `task/` - Task management app
- `comment/` - Comment system app

## Notes

- Default database is SQLite (`db.sqlite3`).
- Static files are served from the `static/` directory in development.
- API authentication uses token-based authentication (`rest_framework.authtoken`).
- Import the API.postman_collection.json file on Postman to use all the endpoints.