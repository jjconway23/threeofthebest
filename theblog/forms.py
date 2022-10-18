from django import forms
from .models import Post, Category
#, Comment
choices = Category.objects.all().values_list('name','name')
choices_list = []

for item in choices:
	choices_list.append(item)

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'category', 'snippet', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'form-user-id', 'type':'hidden'}),
			'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),			
		}


class UpdatePostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'category', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			#'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
			#'author': forms.Select(attrs={'class': 'form-control'}),
			'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),			
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),			
		}