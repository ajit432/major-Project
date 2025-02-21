from django import forms
from HR.models import Student_Ratings_Data


class StudentMockForms(forms.ModelForm):
    class Meta:
        model = Student_Ratings_Data
        exclude =['conducted_by']
