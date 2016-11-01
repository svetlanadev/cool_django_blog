from django import forms
from blog.models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=94, help_text="Please enter the title of Post.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Post
        fields = ('title', 'body',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
