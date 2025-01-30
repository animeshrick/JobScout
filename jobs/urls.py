from django.urls import path

from jobs.view.add_jobs import AddJobView

urlpatterns = [
    path("create-users", AddJobView.as_view(), name="Add-Job"),
]
