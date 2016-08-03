from django import forms
from .models import Articles, Comments

class CommentForm(forms.ModelForm):

	writer = forms.CharField(max_length=150,
		error_messages={
        'required':'پر کردن این فیلد الزامی است.', 'invalid':'مقدار وارد شده صحیح نمیباشد.'}, 
         widget=forms.TextInput(attrs={
          'class' : 'form-control' ,'aria-describedby':'basic-addon1', 'style' : 'width:300px' }))
	

	text = forms.CharField(required=True, widget=forms.Textarea(attrs={
		'rows' : '6', 'style' : 'width:300px' ,'class' : 'form-control' ,'aria-describedby':'basic-addon1',
		}), 
		error_messages={
        'required':'پر کردن این فیلد الزامی است.', 'invalid':'مقدار وارد شده صحیح نمیباشد.'})

	class Meta:
		model = Comments
		fields = ['text', 'writer']


