from django.shortcuts import render, redirect
from .models import SkillExchange
from .models import JobPost
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .forms import JobPostForm, SkillExchangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import CustomUserCreationForm

def logout_view(request):
    logout(request)
    return redirect('home')
def home(request):
    jobs = JobPost.objects.all()
    skills = SkillExchange.objects.all()
    return render(request, 'home.html', {'jobs': jobs, 'skills': skills})

@login_required
def create_job_post(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('home')
    else:
        form = JobPostForm()
    return render(request, 'create_job_post.html', {'form': form})

@login_required
def create_skill_exchange(request):
    if request.method == 'POST':
        form = SkillExchangeForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.posted_by = request.user
            skill.save()
            return redirect('home')
    else:
        form = SkillExchangeForm()
    return render(request, 'create_skill_exchange.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home')  # Redirect to the homepage
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})