from django.contrib import admin
from .models import JobPost, SkillExchange

@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'posted_by', 'date_posted')
    search_fields = ('title', 'location', 'posted_by__username')
    list_filter = ('date_posted', 'location')

@admin.register(SkillExchange)
class SkillExchangeAdmin(admin.ModelAdmin):
    list_display = ('skill_offered', 'skill_requested', 'posted_by', 'date_posted')
    search_fields = ('skill_offered', 'skill_requested', 'posted_by__username')
    list_filter = ('date_posted',)

from .forms import JobPostAdminForm, SkillExchangeAdminForm

class JobPostAdmin(admin.ModelAdmin):
    form = JobPostAdminForm


class SkillExchangeAdmin(admin.ModelAdmin):
    form = SkillExchangeAdminForm
