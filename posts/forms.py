from django import forms 
from .models import Post
from time import gmtime, strftime
from blog.helpers import Helpers
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class PostAddForm(forms.Form):
	title = forms.CharField(max_length = 120)
	description = forms.CharField(widget=forms.Textarea)
	file = forms.FileField(validators=[
		FileExtensionValidator(['jpg', 'jpeg', 'png'], 'The file can only be in png or jpg format')
	])
	title.widget.attrs.update({'class': 'form-control'})
	description.widget.attrs.update({'class': 'form-control'})
	file.widget.attrs.update({'class': 'custom-file-input'})
	
	def save(self, user_id):
		Post.objects.create(
			title=self.cleaned_data['title'],
			description=self.cleaned_data['description'],
			img_path=Helpers.loadFile(self.cleaned_data['file']),
			date=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
			owner_id = user_id

			)
class PostEditForm(forms.Form):
	title = forms.CharField(max_length = 120)
	description = forms.CharField(widget=forms.Textarea)
	file = forms.FileField(required=False, validators=[
		FileExtensionValidator(['jpg', 'jpeg', 'png'], 'The file can only be in png or jpg format')
	])
	title.widget.attrs.update({'class': 'form-control'})
	description.widget.attrs.update({'class': 'form-control'})
	file.widget.attrs.update({'class': 'custom-file-input'})






		


