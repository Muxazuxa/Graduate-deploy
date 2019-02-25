from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from .models import Student, Cafedra, Faculty
from .forms import StudentForm
from .filters import StudentFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class StudentCreateView(LoginRequiredMixin, CreateView):
    redirect_field_name = 'student/login'
    template_name = 'student/create.html'
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return "list"


class StudentListView(LoginRequiredMixin, ListView):
    redirect_field_name = 'student/login'
    context_object_name = 'students'
    template_name = 'student/list.html'

    def get_queryset(self):
        return Student.objects.all()


@login_required(redirect_field_name='student/login')
def load_cafedra(request):
    faculty_id = request.GET.get('faculty')
    cafedra = Cafedra.objects.filter(faculty_id=faculty_id).order_by('name')
    return render(request, 'student/cafedra_dropdown_list_options.html', {'cafedra': cafedra})


@login_required(redirect_field_name='student/login')
def search(request):
    student_list = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset=student_list)
    return render(request, 'student/search.html', {'filter': student_filter})

