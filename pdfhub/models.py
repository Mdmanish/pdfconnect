from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    pincode = models.CharField(max_length=6, blank=True, null=True)
    roll_number = models.CharField(max_length=50, blank=True, null=True)
    registration_number = models.CharField(max_length=50, blank=True, null=True)
    class_name = models.CharField(max_length=100, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    school_board = models.CharField(max_length=100, blank=True, null=True)
    school_address = models.TextField(blank=True, null=True)


class UploadedFile(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='pdf_files/')
    # source_id = models.CharField(max_length=100)
