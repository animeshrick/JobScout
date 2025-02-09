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

from django.urls import path

from job_applications.view.create_job_application import CreateJobApplicationView
from job_applications.view.get_application_by_id import GetJobApplicationByIDView

urlpatterns = [
    path(
        "create-application",
        CreateJobApplicationView.as_view(),
        name="Create-Job-Application",
    ),
    path(
        "get-application",
        GetJobApplicationByIDView.as_view(),
        name="Get-Job-Application",
    ),
]
