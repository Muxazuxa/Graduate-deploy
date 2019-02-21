from django.urls import path
from . import views
from django_filters.views import FilterView
from .filters import StudentFilter
from django.contrib.auth import views as auth_views
from django.conf.urls import url

app_name = 'student'

urlpatterns = [
    path('add', views.StudentCreateView.as_view(), name='add'),
    path('list', views.StudentListView.as_view(), name='list'),
    path('greet', views.greet, name='greet'),
    path('ajax/load-cafedra/', views.load_cafedra, name='ajax_load_cafedra'),
    path('search', FilterView.as_view(filterset_class=StudentFilter, template_name='student/search.html'), name='search'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='student/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='student/logout.html'), name='logout'),
]
