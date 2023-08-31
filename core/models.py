from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

class ProjectPeakAcademia(models.Model):
    facebook_url = models.URLField(max_length=10000, null=True, blank=True)
    instagram_username = models.CharField(max_length=10000, null=True, blank=True)
    twitter_username = models.CharField(max_length=10000, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=10000, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=10000, null=True, blank=True)
    phone_number = models.CharField(max_length=10000, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    account_number = models.CharField(null=True, blank=True)
    account_name = models.CharField(max_length=10000, null=True, blank=True)
    bank_name = models.CharField(max_length=10000, null=True, blank=True)


class Course(models.Model):
    name = models.CharField(max_length=10000)
    projects_count = models.IntegerField(default=0, editable=False) 
    url = models.SlugField(max_length=10000, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Project(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=10000)
    format = models.CharField(max_length=10000)
    chapters = models.IntegerField()
    pages = models.IntegerField()
    price = models.IntegerField()
    rating = models.DecimalField(decimal_places=1, max_digits=3)
    users_that_found_this_project_useful = models.IntegerField()
    abstract = models.TextField() 
    url = models.SlugField(max_length=10000, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project_Request(models.Model):
    name = models.CharField(max_length=10000, null=True, blank=True)
    phone_number = models.IntegerField()
    course_of_study = models.CharField(max_length=10000, null=True, blank=True)
    email = models.CharField(max_length=10000, null=True, blank=True)
    education_level = models.CharField(max_length=10000, null=True, blank=True)
    project_title = models.CharField(max_length=10000, null=True, blank=True)
    project_details = models.TextField()

class Our_Services(models.Model):
    service = models.CharField(max_length=10000)
    service_description = models.TextField()


@receiver(post_save, sender=Project)
def update_projects_count(sender, instance, **kwargs):
    course = instance.course
    projects_count = course.project_set.count()
    course.projects_count = projects_count
    course.save()
