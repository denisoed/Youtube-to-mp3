from django import forms
from .models import youtubeModel

class YoutubeForms(forms.ModelForm):

    class Meta:
        model = youtubeModel
        fields = ('url', 'email',)
        widgets = {'url': forms.TextInput(attrs={'placeholder': 'Url address...'}), 'email': forms.TextInput(attrs={'placeholder': 'Email address...'})}
