from django.contrib import admin
from core.models import Course, Project, ProjectPeakAcademia, Project_Request, Our_Services
# Register your models here.
admin.site.register(ProjectPeakAcademia)
admin.site.register(Course)
admin.site.register(Project)
admin.site.register(Project_Request)
admin.site.register(Our_Services)
