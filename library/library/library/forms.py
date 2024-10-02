# forms.py
from django import forms
from .models import BookIssue

# class BookIssueForm(forms.ModelForm):
#     class Meta:
#         model = BookIssue
#         fields = ['first_name', 'last_name', 'book_name', 'author', 'issue_date']
from django import forms
from .models import BookIssue

class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['first_name', 'last_name', 'book_name', 'author', 'issue_date', 'return_date']
