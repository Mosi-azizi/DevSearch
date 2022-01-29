from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutUser, name='logout'),
    path('register/',views.registerUser, name='register'),
    path('', views.profiles,name='profiles'),
    path('profile/<str:pk>/',views.userProfile, name='user-profile'),
    path('account/',views.userAccount, name='account'),
    path('edit-account/',views.editAccount, name = 'edit-account'),
    path('create-skill/',views.createSKill, name= 'create-skill'),
    path('update-skill/<str:pk>/',views.updateSKill, name= 'update-skill'),
    path('delete-skill/<str:pk>/',views.deleteSkill, name= 'delete-skill'),
    path('inbox/',views.inbox, name='inbox'),
    path('message/<str:pk>/',views.viewMessage, name = 'message'),
    path('send-message/<str:pk>/',views.createMessage, name='create-message'),
]