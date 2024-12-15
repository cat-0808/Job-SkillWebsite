from django import forms
from .models import JobPost, SkillExchange
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JobPostAdminForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'

class SkillExchangeAdminForm(forms.ModelForm):
    class Meta:
        model = SkillExchange
        fields = '__all__'
class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['title', 'description', 'location']

class SkillExchangeForm(forms.ModelForm):
    class Meta:
        model = SkillExchange
        fields = ['skill_offered', 'skill_requested', 'description']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']