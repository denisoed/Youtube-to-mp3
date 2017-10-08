from django import forms
from .models import youtubeModel

class YoutubeForms(forms.ModelForm):

    class Meta:
        model = youtubeModel
        fields = ('url', 'email',)
