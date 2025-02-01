from users.models.base_models.base_model import GenericBaseModel
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Job(GenericBaseModel):
    JOB_STATUS = (
        ("start", "Actively Hiring"),
        ("end", "Hiring finished"),
    )

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    locations = models.JSONField(default=list)
    skills = models.JSONField(default=list)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    experience = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    notice_period = models.CharField(max_length=255, null=True, blank=True)
    vacancy = models.IntegerField(
        null=True, blank=True, validators=[MaxValueValidator(255), MinValueValidator(0)]
    )
    good_to_have = models.CharField(max_length=255, null=True, blank=True)
    industry_type = models.CharField(max_length=255, null=True, blank=True)
    employment_type = models.CharField(max_length=255, null=True, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)

    description = models.TextField()
    # posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")

    status = models.CharField(
        max_length=10, choices=JOB_STATUS, default="start", null=False, blank=False
    )

    def __str__(self):
        return f"{self.title} at {self.company}"
