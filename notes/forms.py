from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
  class Meta:
    model = Notes
    fields = ('title', 'text')
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
      'text': forms.Textarea(attrs={'class': 'form-control mb-5'}),
    }
    labels = {
      'text': 'Write your note here',
    }

  def clean_title(self):
    title = self.cleaned_data.get('title')
    if 'Django' not in title:
      raise forms.ValidationError("Title must contain the word 'Django'.")
    return title
