from .models import Student
import django_filters


class StudentFilter (django_filters.FilterSet):

    fio=django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ('fio', 'faculty', 'cafedra', 'jcategory', 'graduate_date')
