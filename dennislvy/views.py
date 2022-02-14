

from django.shortcuts import render,redirect
from .models import Project , Tag
from django.views.generic import ListView
from .forms import ProjectForm,ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .utils import searchProjects,paginatProjects
# Create your views here.


def projects(request):
    projects , search_query = searchProjects(request)
    custom_range , projects = paginatProjects(request, projects , 3)

    context = {'projects': projects,'search_query':search_query , 'custom_range':custom_range }
    return  render(request,'projects/projects.html',context)


def project (request, pk):
    projectobj = Project.objects.get(id=pk)
    tags = projectobj.tags.all()
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectobj
        review.owner = request.user.profile
        review.save()
        # update project votecount
        projectobj.getVoteCount

        messages.success(request , 'Your review was successfully submitted!')
        return redirect('dennislvy:project', pk=projectobj.id)

    print('projectobj',projectobj)
    return render(request,'projects/single-project.html',{'project':projectobj,'tags':tags , 'form':form})

class ProjectListView(ListView):
    model = Project
    template_name = 'projects/projectslv.html'
    context_object_name = 'projectslv'

@login_required(login_url='users:login')
def createProject(request, pk):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('users:account')
    context = {
        'form':form
    }
    return  render(request,'projects/project_form.html',context)

@login_required(login_url='users:login')
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('users:account')
    context = {
        'form':form,
        'project':project
    }
    return  render(request,'projects/project_form.html',context)

@login_required(login_url='users:login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()

        return redirect('users:account')

    context ={'object':project}
    return render(request,'projects/delete_object.html',context)
