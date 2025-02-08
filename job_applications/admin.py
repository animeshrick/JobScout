from django.contrib import admin

from job_applications.models.job_application_model import JobApplication

# class JobApplicationAdmin(admin.ModelAdmin):
#     list_display = (
#         "title",
#         "company",
#         "vacancy",
#         "locations",
#         "skills",
#         "posted_by",
#         "created_at",
#     )
#     search_fields = ("company", "locations", "skills", "posted_by")
#

admin.site.register(JobApplication)
