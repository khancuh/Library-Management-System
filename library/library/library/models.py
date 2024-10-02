from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.contrib.auth.models import User

class BookIssue(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    issue_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.book_name}"

class BookIssue(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    issue_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)  # Optional field for return date

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.book_name}"