from django import forms
from .models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = post 
		fields = ('title', 'text', 'author')

class  Post(forms.Form):
	Choices = (('1', 'Me'), ('2', 'You'))
	title = forms.CharField(max_length=200)
	text = forms.TextField()
	author = forms.ChoiceField(choices=Choices)
