from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

class Application(models.Model):
    COURSES = (
    ('Computer Science Engineering', 'Computer Science Engineering'),
    ('Information Technology Engineering', 'Information Technology Engineering'),
    ('Electronics and Telecommunication Engineering', 'Electronics and Telecommunication Engineering'),
    ('Electronics Engineering', 'Electronics Engineering'),
    )

    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.CharField(max_length=100, choices= COURSES)
    name = models.CharField(max_length=200) 
    email = models.CharField(max_length=200) 
    phone_no = models.CharField(max_length=200) 
    address = models.TextField(max_length=200) 
    student_profile = models.ImageField(upload_to="images") 
    Nationality = models.TextField(max_length=200)
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    idcard = models.ImageField(upload_to="images", null=True)
    birth_certificate = models.ImageField(upload_to="images", null=True)
    KCSE_certificate = models.ImageField(upload_to="images", null=True)
    Medical_Cleareance = models.ImageField(upload_to="images", null=True)
    guardian_name = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200) 
    guardian_email = models.CharField(max_length=200) 
    guardian_phone_no = models.CharField(max_length=200) 
    guardian_address = models.TextField(max_length=200) 
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users')

class Notice(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Detail(models.Model):
    title = models.ForeignKey(Notice, on_delete=models.CASCADE)
    notice = models.CharField(max_length=200)

    def __str__(self):
        return self.notice