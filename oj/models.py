from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_id = models.CharField(max_length=50)
    problem_name = models.CharField(max_length=50)
    problem_content = models.CharField(max_length=1000, default="No description!")