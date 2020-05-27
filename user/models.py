from ckeditor.widgets import CKEditorWidget
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, FileInput, Select

from gezi.models import Gezi


class GeziForm(ModelForm):
    class Meta:
        model = Gezi
        fields = ('title', 'slug', 'category','keywords', 'city', 'image','detail','description')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
            'category': Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'city': TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'description':TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
            'detail': CKEditorWidget(),
        }
