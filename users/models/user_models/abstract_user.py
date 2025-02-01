from django.db import models
from users.models.base_models.base_model import GenericBaseModel


class AbstractUser(GenericBaseModel):
    ROLE_CHOICES = (
        ("seeker", "Job Seeker"),
        ("recruiter", "Recruiter"),
    )

    email = models.EmailField(
        verbose_name="Email", max_length=255, unique=True, null=False
    )
    fname = models.CharField(max_length=255, null=False)
    lname = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True)

    company = models.CharField(max_length=255, null=True, blank=True)

    image = models.CharField(max_length=2555, null=True, blank=True)
    resume = models.CharField(max_length=2555, null=True, blank=True)

    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default="seeker", null=False, blank=False
    )

    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.role})"

    @property
    def get_phone(self):
        """Fetch registered Phone Number of the user"""
        if self.phone:
            return self.phone

    @property
    def get_full_name(self):
        """Fetch registered Phone Number of the user"""
        if self.fname and self.lname:
            return f"{self.fname} {self.lname}"
        else:
            return None

    @property
    def get_is_active(self):
        return self.is_active

    @property
    def get_is_deleted(self):
        return self.is_deleted

    @property
    def get_is_recruiter(self):
        return self.role == "recruiter"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
