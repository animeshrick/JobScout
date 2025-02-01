from django.contrib import admin

from jobs.models.job_model import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "vacancy", "locations", "skills", "created_at")
    # search_fields = ('title', 'company', 'location')
    # list_filter = ('company', 'recruiter', 'location')
    # ordering = ('-posted_at',)
    # list_editable = ('vacancy', 'company')
    # date_hierarchy = 'posted_at'

    # Optionally, you can define fields to display in the form view:
    # fields = ("title", "description", "vacancy", "company", "locations", "salary")
    search_fields = ("company", "locations", "skills")


admin.site.register(Job, JobAdmin)
