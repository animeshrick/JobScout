"""
URL configuration for JobScout project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>JobScout - Find Your Dream Job</title>
        <style>
            /* General Styles */
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }

            header {
                background-color: #0073b1;
                color: white;
                padding: 10px 20px;
                text-align: center;
            }

            header h1 {
                margin: 0;
            }

            nav a {
                color: white;
                text-decoration: none;
                margin: 0 10px;
            }

            /* Hero Section */
            .hero {
                background-color: #0073b1;
                color: white;
                padding: 50px 20px;
                text-align: center;
            }

            .hero h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
            }

            .hero p {
                font-size: 1.2rem;
                margin-bottom: 20px;
            }

            .search-form {
                display: flex;
                justify-content: center;
                gap: 10px;
            }

            .search-form input {
                padding: 10px;
                width: 300px;
                border: none;
                border-radius: 5px;
            }

            .search-form button {
                padding: 10px 20px;
                background-color: #ff6b6b;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            .search-form button:hover {
                background-color: #ff4c4c;
            }

            /* Features Section */
            .features {
                display: flex;
                justify-content: space-around;
                padding: 40px 20px;
                background-color: white;
            }

            .feature {
                text-align: center;
                width: 30%;
            }

            .feature h2 {
                font-size: 1.5rem;
                margin-bottom: 10px;
            }

            .feature p {
                font-size: 1rem;
                color: #666;
            }

            /* Footer */
            footer {
                background-color: #333;
                color: white;
                text-align: center;
                padding: 10px 0;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>JobScout</h1>
        </header>

        <div class="hero">
            <h1>Welcome to JobScout</h1>
            <p>Your gateway to finding the perfect job.</p>
        </div>

        <div class="features">
            <div class="feature">
                <h2>Explore Jobs</h2>
                <p>Discover thousands of job opportunities tailored to your skills and interests.</p>
            </div>
            <div class="feature">
                <h2>Apply Easily</h2>
                <p>Apply to jobs with just a few clicks and track your applications.</p>
            </div>
            <div class="feature">
                <h2>Get Noticed</h2>
                <p>Let employers find you by creating a standout profile.</p>
            </div>
        </div>

        <footer>
            <p>&copy; 2025 JobScout. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """
    return HttpResponse(html_content)


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("auth/api/v2/", include("users.urls")),
    path("job/api/v2/", include("jobs.urls")),
    path("application/api/v2/", include("job_applications.urls")),
    path("upload/api/v2/", include("upload.urls")),
]
