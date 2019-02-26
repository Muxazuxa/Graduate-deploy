from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from student.models import Student, Cafedra, Faculty
from student.forms import StudentForm


class GradCreateView(CreateView):
    template_name = 'global/add.html'
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return "success"


def greet(request):
    return render(request, 'global/greet.html')


def about(request):
    return render(request, 'global/about.html')


def success(request):
    return render(request, 'global/success.html')


def load_cafedra(request):
    faculty_id = request.GET.get('faculty')
    cafedra = Cafedra.objects.filter(faculty_id=faculty_id).order_by('name')
    return render(request, 'global/cafedra_dropdown_list_options.html', {'cafedra': cafedra})