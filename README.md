# JobScout Backend API

JobScout is a simple Job Board API built using Django and Django REST Framework (DRF). This API allows users to manage job postings and applications efficiently. The project follows industrial standards and is hosted on a live database.

### Features

- CRUD operations for job postings
- User authentication and token-based authorization
- API documentation with DRF
- Hosted on a live database
- Installation
- Prerequisites: Python 3.x, Django, Django REST Framework, PostgreSQL (or any preferred database)
- Setup Instructions

## Clone the repository
git clone https://github.com/animeshrick/JobScout.git
cd jobscout

## Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install dependencies
pip install -r requirements.txt

## Setup environment variables (configure .env file accordingly)
export DATABASE_URL=your_database_url

## Run migrations
python manage.py migrate

## Create a superuser
python manage.py createsuperuser

## Start the development server
python manage.py runserver

---

#### LIVE ENDPOINT: https://jobscout-k438.onrender.com
#### API Documents: https://documenter.getpostman.com/view/11672475/2sAYX9oLXJ


---

## API Endpoints

---

### Authentication

| Method | Endpoint                       | Description           |
|--------|--------------------------------|-----------------------|
| POST   | `/auth/api/v2/create-users`    | Register a new user   |
| POST   | `/auth/api/v2/sign-in`         | Login and get a token |
| POST   | `/auth/api/v2/send-otp/`       | Send OTP              |
| POST   | `/auth/api/v2/verify-otp`      | Verify OTP            |
| POST   | `/auth/api/v2/update-password` | Update Password       |
| POST   | `/auth/api/v2/reset-password`  | Reset Password        |
| POST   | `/auth/api/v2/remove-user`     | Remove User           |

### Jobs

| Method | Endpoint                            | Description                    |
|--------|-------------------------------------|--------------------------------|
| POST   | `job/api/v2/add-job`                | Register a new Job             |
| POST   | `job/api/v2/job-info`               | Information about specific job |
| POST   | `job/api/v2/update-job`             | Update a Job                   |
| POST   | `job/api/v2/remove-job`             | Remove a Job                   |
| POST   | `job/api/v2/get-all-applied-jobs`   | Get all applied Jobs           |
| POST   | `job/api/v2/get-all-created-jobs`   | Get all created Jobs           |
| POST   | `job/api/v2/job-filter`             | Filter Jobs                    |
| POST   | `job/api/v2/get-jobs`               | Get all jobs                   |

### Job Applications

| Method | Endpoint                                          | Description              |
|--------|---------------------------------------------------|--------------------------|
| POST   | `application/api/v2/create-application`           | Apply for a Job          |
| POST   | `application/api/v2/get-application`              | Get applied application  |
| POST   | `application/api/v2/withdraw`                     | Withdraw job application |

### Upload CV & Profile Image

| Method | Endpoint                                          | Description              |
|--------|---------------------------------------------------|--------------------------|
| POST   | `upload/api/v2/upload-file`           | Upload Image & CV        |


## Development

### Run Tests

Run the test suite to ensure everything works as expected:

```bash
$ pytest
```

### Linting

Ensure code quality by running a Cleaner:

```bash
$ clean.bat
```

---


## Folder Structure

```
.
├── JobScout/             # Django project folder
├── users/                # App for user managment
├── jobs/                 # App for managing expenses
├── job_applications/     # App for managing friends and friend requests
├── upload/               # to upload files
```

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Thanks to the Django and Django Rest Framework teams for their amazing tools.
- Special thanks to contributors and testers.

---

For any queries, feel free to reach out to job.scout.2025@gmail.com. We’ll get back to you as soon as possible!
