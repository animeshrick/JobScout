# from users.models.base_models.base_model import GenericBaseModel
# from django.db import models
#
#
# class JobApplication(GenericBaseModel):
#     STATUS_CHOICES = (
#         ("pending", "Pending"),
#         ("reviewed", "Reviewed"),
#         ("accepted", "Accepted"),
#         ("rejected", "Rejected"),
#     )
#
#     job = models.ForeignKey("jobs.Job", on_delete=models.CASCADE, related_name="applications")
#     applicant = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="applications")
#     # job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
#     # applicant = models.ForeignKey(
#     #     User, on_delete=models.CASCADE, related_name="applications"
#     # )
#     cover_letter = models.TextField(blank=True, null=True)
#     resume = models.FileField(upload_to="applications/resumes/", blank=True, null=True)
#     applied_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
#
#     class Meta:
#         app_label = "jobs"
#         unique_together = ("job", "applicant")
#
#     def __str__(self):
#         return f"{str(self.applicant)} applied for {str(self.job)}"
#
