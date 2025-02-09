JobScout API

JobScout is a simple Job Board API built using Django and Django REST Framework (DRF). This API allows users to manage job postings and applications efficiently. The project follows industrial standards and is hosted on a live database.

Features

CRUD operations for job postings

User authentication and token-based authorization

API documentation with DRF

Hosted on a live database

Installation

Prerequisites

Python 3.x

Django

Django REST Framework

PostgreSQL (or any preferred database)

Setup Instructions

# Clone the repository
git clone https://github.com/your-username/jobscout.git
cd jobscout

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Setup environment variables (configure .env file accordingly)
export DATABASE_URL=your_database_url

# Run migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver

API Endpoints

Authentication

POST /api/auth/register/ - Register a new user

POST /api/auth/login/ - Login and obtain an access token

Job Listings

GET /api/jobs/ - Retrieve all job listings

POST /api/jobs/ - Create a new job (requires authentication)

GET /api/jobs/{id}/ - Retrieve a specific job

PUT /api/jobs/{id}/ - Update a job (requires authentication)

DELETE /api/jobs/{id}/ - Delete a job (requires authentication)

Applications

GET /api/applications/ - Retrieve all applications (admin only)

POST /api/jobs/{id}/apply/ - Apply for a job

GET /api/applications/{id}/ - Retrieve a specific application

Deployment

The API is hosted on a live server.

Use gunicorn and nginx for production setup.

Configure environment variables for production.

Contributing

Feel free to contribute to the project by opening issues or submitting pull requests.

License

This project is licensed under the MIT License.

For further details, refer to the official documentation.

