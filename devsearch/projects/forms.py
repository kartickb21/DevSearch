from django.forms import ModelForm, fields, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),        
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        #self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add Title'})
        for name, fields in self.fields.items():
            fields.widget.attrs.update({'class':'input'})
