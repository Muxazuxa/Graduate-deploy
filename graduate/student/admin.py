from django.contrib import admin
from .models import Cafedra, Faculty, Student, JCategory, Photo

# Register your models here.


class AdminProfile(admin.ModelAdmin):
    list_display = ('fio', 'faculty', 'cafedra', 'graduate_date', 'telephone', 'email')
    search_fields = ('fio',)

    def get_queryset(self, request):
        queryset = super(AdminProfile, self).get_queryset(request)
        queryset = queryset.order_by('-fio')
        return queryset


admin.site.register(Student, AdminProfile)
admin.site.register(Cafedra)
admin.site.register(Faculty)
admin.site.register(JCategory)
admin.site.register(Photo)
