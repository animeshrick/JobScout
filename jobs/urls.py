from django.urls import path

from jobs.view.add_jobs import AddJobView
from jobs.view.all_jobs import AllJobsView

urlpatterns = [
    path("add-job", AddJobView.as_view(), name="Add-Job"),
    path("get-jobs", AllJobsView.as_view(), name="Get-All-Jobs"),
]
