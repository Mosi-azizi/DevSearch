from django.forms import  models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Skill,Message

class CustomUserCreationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args , **kwargs):
        super(CustomUserCreationsForm,self).__init__(*args , **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','bio','short_intro','profile_images','social_github','social_twitter','social_website',
                  'social_linkedin',]

    def __init__(self, *args , **kwargs):
        super(ProfileForm,self).__init__(*args , **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SkillForm(models.ModelForm):
    class Meta:
        model = Skill
        fields = ['name','description']

    def __init__(self, *args , **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class MessageForm(models.ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})