from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def uc(request):
    return render(request, 'uc.html')

def projects(request):
    statuses = Status.objects.all().values()
    projects = Projects.objects.all().order_by('name')
    context = {
        'statuses': statuses,
        'projects': projects,
    }
    return render(request, 'projects.html', context)

def codeOfConduct(request):
    return render(request, 'conduct.html')

def members(request):
    roles = Role.objects.all().values()
    members = Members.objects.all().values()
    context = {
        'roles': roles,
        'members': members,
    }
    return render(request, 'members.html', context)

def join(request):
    return render(request, 'join.html')

def viewProject(request, project_id):
    project = Project.objects.get(id=project_id)
    statuses = Status.objects.all().values()
    context = {
        'project': project,
        'statuses': statuses,
    }
    return render(request, 'viewProject.html')