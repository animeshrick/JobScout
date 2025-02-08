from users.models.base_models.base_model import GenericBaseModel
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

from users.models.user_models.user import User


class Job(GenericBaseModel):
    JOB_STATUS = (
        ("start", "Actively Hiring"),
        ("end", "Hiring finished"),
    )

    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    locations = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
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
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posted_by", null=True, blank=True
    )

    description = models.CharField(max_length=1000, null=True, blank=True)
    jd = models.CharField(max_length=500, null=True, blank=True)

    status = models.CharField(
        max_length=10, choices=JOB_STATUS, default="start", null=False, blank=False
    )

    applicants = models.ManyToManyField(User, related_name="applied_jobs", blank=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} at {self.company}"

    def save(self, *args, **kwargs):
        if isinstance(self.locations, list):
            self.locations = ",".join(self.locations)  # Convert list to string

        if isinstance(self.skills, list):
            self.skills = ",".join(self.skills)  # Convert list to string

        super().save(*args, **kwargs)

    def get_applicants_list(self):
        return list(self.applicants.all())
