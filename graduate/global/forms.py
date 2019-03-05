from django import forms
from student.models import Student, Cafedra


class GradForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = (
            'fio',
            'graduate_date',
            'faculty',
            'cafedra',
            'country',
            'job',
            'jcategory',
            'telephone',
            'email',
            'feedback')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cafedra'].queryset = Cafedra.objects.none()
        self.fields['fio'].widget.attrs.update(size='30')

        if 'faculty' in self.data:
            try:
                faculty_id = int(self.data.get('faculty'))
                self.fields['cafedra'].queryset = Cafedra.objects.filter(faculty_id=faculty_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['cafedra'].queryset = self.instance.faculty.cafedra_set.order_by('name')

