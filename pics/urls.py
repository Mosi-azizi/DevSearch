from django.urls import path,reverse_lazy
from . import views
from django.views.generic import TemplateView

app_name = 'pics'

urlpatterns = [
    path('pics/',views.PicListView.as_view(), name='all'),
    path('pic/<int:pk>',views.PicDetailView.as_view(),name ='pic_detail'),
    path('pic_picture',views.stream_file, name='pic_picture'),
    path('pic/create',views.PicCreateView.as_view(), name='pic_create'),
]