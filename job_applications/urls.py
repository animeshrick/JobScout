from django.urls import path

from job_applications.view.create_job_application import CreateJobApplicationView
from job_applications.view.get_application_by_id import GetJobApplicationByIDView
from job_applications.view.withdraw_job_application import WithdrawJobApplicationView

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
    path(
        "withdraw",
        WithdrawJobApplicationView.as_view(),
        name="Withdraw-Job-Application",
    ),
]
