from django.contrib import admin

from jobs.models.job_model import Job


class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "vacancy",
        "locations",
        "skills",
        "posted_by",
        "created_at",
    )
    search_fields = ("company", "locations", "skills", "posted_by")


admin.site.register(Job, JobAdmin)
