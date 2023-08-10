from django.contrib import admin
from core.models import Course, Project, ProjectPeakAcademia, Project_Request, Our_Services

# Register your models here.
admin.site.site_header = 'ProjectPeak Academia Admin'
admin.site.site_title = 'ProjectPeak Academia Admin Panel'
admin.site.index_title = 'Welcome to ProjectPeak Academia Admin'

class ProjectAdmin(admin.ModelAdmin): 
    search_fields = ('name',)
    list_filter = ('course','format','price')

class CourseAdmin(admin.ModelAdmin): 
    search_fields = ('name',)

class Our_ServicesAdmin(admin.ModelAdmin): 
    search_fields = ('service',)

class Project_RequestAdmin(admin.ModelAdmin): 
    search_fields = ('project_title',)
    list_filter = ('course_of_study','education_level')

admin.site.register(ProjectPeakAcademia)
admin.site.register(Course, CourseAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Project_Request, Project_RequestAdmin)
admin.site.register(Our_Services, Our_ServicesAdmin)
