from users.models.base_models.base_model import GenericBaseModel
from django.db import models

from users.models.user_models.user import User


class Job(GenericBaseModel):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")

    def __str__(self):
        return f"{self.title} at {self.company}"
