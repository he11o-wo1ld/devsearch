from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from .models import Project, Tag
from .forms import ProjectForm
from .utils import *

def projects(request):
    projects, search_query = searchProjects(request)

    context = {'projects':projects, 'search_query': search_query}
    return render(request, 'project/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'project/single-project.html', {'project': projectObj})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, "Skill Has Been Created  Successfully.!")
            return redirect('account')

    context = {'form': form}
    return render(request, "project/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill Has Been Updated  Successfully.!")
            return redirect('account')

    context = {'form': form}
    return render(request, "project/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Skill Has Been Deleted  Successfully.!")
        return redirect('account')
    context = {'object': project}
    return render(request, "delete_template.html", context)
