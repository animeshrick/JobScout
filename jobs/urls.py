from django.urls import path

from jobs.view.add_jobs import AddJobView
from jobs.view.all_jobs import AllJobsView
from jobs.view.filter_jobs import FilterJobsView
from jobs.view.get_all_applied_jobs import GetAllAppliedJobsView
from jobs.view.get_all_created_jobs import GetAllCreatedJobsView
from jobs.view.get_job_by_id import GetJobByIDView
from jobs.view.remove_job import RemoveJobView
from jobs.view.update_job import UpdateJobView

urlpatterns = [
    path("add-job", AddJobView.as_view(), name="Add-Job"),
    path("get-jobs", AllJobsView.as_view(), name="Get-All-Jobs"),
    path("update-job", UpdateJobView.as_view(), name="Update-Job"),
    path("remove-job", RemoveJobView.as_view(), name="Remove-Job"),
    path(
        "get-all-created-jobs",
        GetAllCreatedJobsView.as_view(),
        name="Get-All-Created-Jobs",
    ),
    path(
        "get-all-applied-jobs",
        GetAllAppliedJobsView.as_view(),
        name="Get-All-Applied-Jobs",
    ),
    path(
        "job-info",
        GetJobByIDView.as_view(),
        name="Get-Jobs-By-ID",
    ),
    path(
        "job-filter",
        FilterJobsView.as_view(),
        name="Get-Filtered-Jobs",
    ),
]
