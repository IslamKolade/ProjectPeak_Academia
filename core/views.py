from django.shortcuts import render, get_object_or_404
from .models import Course, Project, ProjectPeakAcademia, Project_Request
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.

def home(request):
    courses = Course.objects.all().order_by("name")
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'index.html', {'courses': courses, 'projectpeak_academia': projectpeak_academia})

def all_courses(request):
    courses = Course.objects.all().order_by("name")
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'all_courses.html', {'courses': courses, 'projectpeak_academia': projectpeak_academia})

def all_projects(request):
    projects = Project.objects.all().order_by("name")
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'all_projects.html', {'projects': projects, 'projectpeak_academia': projectpeak_academia})


def about(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'about.html', {'projectpeak_academia': projectpeak_academia})

def faq(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'faq.html', {'projectpeak_academia': projectpeak_academia})


def features(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'features.html', {'projectpeak_academia': projectpeak_academia})

def testimonials(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'testimonials.html', {'projectpeak_academia': projectpeak_academia})

def contact(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'contact.html', {'projectpeak_academia': projectpeak_academia})



def course_projects(request, course_slug):
    course = get_object_or_404(Course, url=course_slug)
    projects = Project.objects.filter(course=course)
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    return render(request, 'projects.html', {'course': course, 'projects': projects, 'projectpeak_academia': projectpeak_academia})


def project_details(request, project_slug):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    project = get_object_or_404(Project, url=project_slug)
    project.users_that_found_this_project_useful += 1
    project.save()

    related_projects = Project.objects.filter(course=project.course).exclude(id=project.id)

    return render(request, 'project_details.html', {'project': project, 'projectpeak_academia': projectpeak_academia, 'related_projects': related_projects})

def search_courses(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    query = request.GET.get('q-courses')
    if query:
        results = Course.objects.filter(name__icontains=query)
    else:
        results = []

    return render(request, 'search_course_result.html', {'query': query, 'results': results, 'projectpeak_academia': projectpeak_academia})

def search_course_projects(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    query = request.GET.get('q-projects')
    query_course = request.GET.get('q-course_projects')
    if query:
        course_name = get_object_or_404(Course, name=query_course)
        course = Project.objects.filter(course=course_name)
        results = course.filter(name__icontains=query)
    else:
        results = []
    return render(request, 'search_course_projects_result.html', {'course_name': course_name, 'query': query, 'query_course': query_course, 'results': results, 'projectpeak_academia': projectpeak_academia})


def search_projects(request):
    projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)
    query = request.GET.get('q-projects')
    if query:
        results = Project.objects.filter(name__icontains=query)
    else:
        results = []
    return render(request, 'search_project_result.html', {'query': query, 'results': results, 'projectpeak_academia': projectpeak_academia})


def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        education_level = request.POST.get('education_level')
        project_title = request.POST.get('project_title')
        project_details = request.POST.get('project_details')
        course_of_study = request.POST.get('course_of_study')

        project_request = Project_Request(
            name=name,
            email=email,
            phone_number=phone_number,
            education_level=education_level,
            project_title=project_title,
            project_details=project_details,
            course_of_study=course_of_study,
        )
        project_request.save()

        projectpeak_academia = get_object_or_404(ProjectPeakAcademia, pk=1)

        email_subject = 'Project Request Received'
        email_body = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'course_of_study': course_of_study,
            'phone_number': phone_number,
            'education_level': education_level,
            'project_title': project_title,
            'project_details': project_details,
            'whatsapp_number' : projectpeak_academia.whatsapp_number,
        })

        # Send the email
        msg = EmailMessage(email_subject, email_body, to=[email, 'projectpeakacademia@gmail.com'])
        msg.content_subtype = 'html'
        msg.send()

        return render(request, 'request_received.html', {'projectpeak_academia': projectpeak_academia})
    else:
        return HttpResponseForbidden()




