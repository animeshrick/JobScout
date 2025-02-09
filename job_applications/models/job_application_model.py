from jobs.models.job_model import Job
from users.models.base_models.base_model import GenericBaseModel
from django.db import models

from users.models.user_models.user import User


class JobApplication(GenericBaseModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("withdrawn", "Withdrawn"),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job")
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    class Meta:
        app_label = "jobs"
        unique_together = ("job", "applicant")

    def __str__(self):
        return f"{str(self.applicant.get_full_name)} applied for {str(self.job.title)} at {str(self.job.company)}"
