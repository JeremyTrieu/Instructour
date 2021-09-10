from django.contrib import admin
from . import models

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'school_address')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code', 'school')

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'school', 'subject', 'rating')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('detail', 'professor_rate', 'professor', 'subject')

admin.site.register(models.School, SchoolAdmin)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.Professor, ProfessorAdmin)
admin.site.register(models.Review, ReviewAdmin)