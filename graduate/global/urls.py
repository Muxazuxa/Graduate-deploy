from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'student'

urlpatterns = [
    path('greet', views.greet, name='greet'),
    path('about', views.about, name='about'),
    path('success', views.success, name='success'),
    path('ajax/load-cafedra/', views.load_cafedra, name='ajax_load_cafedra'),
    path('add', views.GradCreateView.as_view(), name='add'),
]