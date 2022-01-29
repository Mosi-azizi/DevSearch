from django.urls import path,include
from .views import RegisterView
app_name = 'accounts'
urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/',RegisterView.as_view(), name='register')

]