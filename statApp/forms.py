from dataclasses import field
from django.forms import ModelForm
from .models import Project

#class for Form
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['nameProject', 'projectProgress', 'link_site']