from django.shortcuts import render,redirect
from .models import Profile,Skill,Message
from dennislvy.models import Project
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import CustomUserCreationsForm,ProfileForm,SkillForm,MessageForm
from .utils import searchProfiles,paginatProfiles
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('users:profiles')

    if request.method == 'POST':
        # print(request.POST)
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            # print('Username dose not exist!')
            messages.error(request, 'Username dose not exist!')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'users:account')
        else:
            # print('Username OR password is incorrect')
            messages.error(request, 'Username OR password is incorrect')
    context = {
        'page':page
    }
    return render(request,'users/login-register.html',context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return  redirect('users:login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationsForm()

    if request.method == 'POST':
      form = CustomUserCreationsForm(request.POST)
      if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request,user)
            return redirect('users:edit-account')
      else:
          messages.success(request, 'an error has occurred during registration')
    context = {
       'page':page, 'form':form
    }
    return render(request,'users/login-register.html',context)

def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range , profiles = paginatProfiles(request, profiles , 1)

    context = {'profiles':profiles,'search_query':search_query , 'custom_range':custom_range}
    return  render(request,'users/profiles.html',context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        'profile':profile,
        'topSkills':topSkills,
        'otherSkills':otherSkills
    }
    return render(request,'users/user-profile.html',context)

@login_required(login_url='/users/login')
def userAccount(request):
    profile = request.user.profile
    projects = profile.project_set.all()
    skills = profile.skill_set.all()
    context = { 'profile':profile, 'skills':skills, 'projects':projects}
    return  render(request,'users/account.html',context)



@login_required(login_url='/users/login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('users:account')
    context = {
        'form':form
    }
    return render(request,'users/profile_form.html',context)

@login_required(login_url='/users/login')
def createSKill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request,'Skill was added successfully')
            return redirect('users:account')

    context = {
        'form':form
    }
    return  render(request,'users/skill_form.html',context)


@login_required(login_url='/users/login')
def updateSKill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            skill.owner = profile
            skill.save()
            messages.success(request, 'Skill was updated successfully')
            return redirect('users:account')

    context = {
        'form':form
    }
    return  render(request,'users/skill_form.html',context)

@login_required(login_url='/users/login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('users:account')
    context = {'object':skill}
    return render(request,'delete_template.html',context)

@login_required(login_url='users:login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests':messageRequests,'unreadCount':unreadCount}
    return render(request, 'users/inbox.html',context)


@login_required(login_url='users:login')
def viewMessage(request , pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {
        'message':message
    }
    return render(request,'users/message.html',context)

# @login_required(login_url='users:login')
def createMessage(request, pk):

    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    try :
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email

            message.save()

            messages.success(request, 'Your message was successfully send')
            return redirect('users:user-profile', pk=recipient.id)

    context ={'recipient':recipient,'form':form}
    return render(request, 'users/message_form.html', context)