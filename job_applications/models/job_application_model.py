from jobs.models.job_model import Job
from users.models.base_models.base_model import GenericBaseModel
from django.db import models

from users.models.user_models.user import User


class JobApplication(GenericBaseModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("reviewed", "Reviewed"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="applications"
    )
    cover_letter = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to="applications/resumes/", blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    class Meta:
        unique_together = ("job", "applicant")

    def __str__(self):
        return f"{self.applicant.get_full_name} applied for {self.job.title}"
