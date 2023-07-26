from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_form_submission/', views.contact_form_submission, name='contact_form_submission'),
    path('all_courses/', views.all_courses, name='all_courses'),
    path('all_projects/', views.all_projects, name='all_projects'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('features/', views.features, name='features'),
    path('contact/', views.contact, name='contact'),
    path('course/<slug:course_slug>/', views.course_projects, name='course_projects'),
    path('project/<slug:project_slug>/', views.project_details, name='project_details'),
    path('courses_search_result/', views.search_courses, name='search_courses'),
    path('projects_search_result/', views.search_projects, name='search_projects'),
    path('course_projects_search_result/', views.search_course_projects, name='search_course_projects'),
]