# CRUD OPERATIONS

A simple Django application which provides REST API endpoints for performing CRUD (Create, Read, Update, Delete) operations on a User resource.

## Setup Instructions

Follow these steps to set up and run the application:

1. Clone the repository:

   ```bash
   git clone https://github.com/mojnomiya/crud-operations.git
   cd crud-operations
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel (optional):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`. You can access the admin panel at `http://localhost:8000/admin/` to manage users.

## API Endpoints

The application provides the following REST API endpoints:

- **GET /users**: Returns a list of all users.
- **GET /users/`<id>`/**: Returns the user with the specified ID.
- **POST /users/**: Creates a new user with the specified data.
- **DELETE /users/`<id>`/**: Deletes or Updates the user with the specified ID.

 `<id>` == user ID when making requests to specific users.

## Authentication
Not implemented any authentication feature
By default, the application allows any user to access the API endpoints. 

## Technologies Used

- Python
- Django
- Django REST framework
- SQLite

