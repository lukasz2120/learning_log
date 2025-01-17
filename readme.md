# Learning Log

We will create a web application called "Learning Log" that allows users to record information on topics they find interesting, enabling them to create journal entries while exploring new knowledge. The application's homepage will feature a brief description of its functionality, encouraging users to register or log in. After logging in, users will be able to create new topics, add entries, and edit or update existing ones.

## Features

- User authentication and authorization
- CRUD operations for Topics and Entries
- Responsive design

## Technologies Used

- **Python** (Version 3.10.2)
- **Django** (Version 5.1.3)
- **Database**: [SQLite]
- **Other technologies**: (Bootstrap)

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python (>= 3.10.2)
- pip
- [Optional] Virtual environment tools (e.g., `venv`, `virtualenv`)
- [Database software if not using SQLite]

### Steps

1. Clone the repository:
   ```bash
   cd your-repo-name
   git clone https://github.com/lukasz2120/learning_log.git
   ```
[Optional]
2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\Activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
[Optional]
4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open the application in your browser at:
   ```
   http://127.0.0.1:8000/
   ```

## Usage

### Features

- **User Authentication**: Users can log in using a superuser account or create a new account by registering within the application.  
- **Automatic Login**: After registration, users are automatically logged into the application for a seamless experience.  
- **Topic and Entry Management**: Logged-in users can create specific topics and add entries under those topics.  
- **User-Specific Content**: All topics and entries are private and unique to each user, ensuring that only the respective user can view their content.

## Folder Structure

- `learning_log/`: Main project folder containing settings and configuration.
- `learning_logs/`: Main application folder. It contains the main models as well as the management of topics and entries.
- `users`: The second application. It manages authorization, registration and authentication of users.
- `templates/`: HTML templates.
- `db.sqlite3`: SQLite database file (if used).
- `manage.py`: Django management script.

## Testing

To run tests, use the following command:
```bash
python manage.py test
```

