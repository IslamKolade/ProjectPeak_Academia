from django.contrib import admin
from core.models import Course, Project, ProjectPeakAcademia, Project_Request
# Register your models here.
admin.site.register(ProjectPeakAcademia)
admin.site.register(Course)
admin.site.register(Project)
admin.site.register(Project_Request)
