from django.forms import ModelForm
from .models import Project, Review
from django import forms


class ProjectFrom(ModelForm):
    class Meta:
        model = Project
        # fields = '__all__'
        fields = ['title','featured_images','description','demo_link','source_link','tag']

        widgets = {
            'tag' : forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args , **kwargs):
        super(ProjectFrom,self).__init__(*args , **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})
        #
        # self.fields['description'].widget.attrs.update({'class':'input','placeholder':'Add description'})
        # self.fields['demo_link'].widget.attrs.update({'class':'input'})
        # self.fields['source_link'].widget.attrs.update({'class':'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']

        labels = {
               'value': 'Place your vote',
               'body': 'Add a comment with your vote'
           }

    def __init__(self, *args , **kwargs):
        super(ReviewForm,self).__init__(*args , **kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})