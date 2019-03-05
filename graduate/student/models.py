from django.db import models

# Create your models here.


class Faculty(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультет'


class Cafedra(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Направление, специальность'
        verbose_name_plural = 'Направление, специальность'


class JCategory(models.Model):
    jcategory=models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.jcategory

    class Meta:
        verbose_name = 'Сфера деятельности'
        verbose_name_plural = 'Сфера деятельности'


class Student(models.Model):
    fio = models.CharField(max_length=100, blank=False, verbose_name='Ф.И.О.')
    graduate_date = models.CharField(blank=False, max_length=4, verbose_name='Год окончания')
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, verbose_name='Факультет')
    cafedra = models.ForeignKey(Cafedra, on_delete=models.SET_NULL, null=True, verbose_name='Кафедра')
    country = models.CharField(max_length=100, blank=False, default='Кыргызстан', verbose_name='Страна проживания')
    job = models.CharField(max_length=100, blank=False, verbose_name='Место работы')
    jcategory = models.ForeignKey(JCategory, on_delete=models.SET_NULL, null=True, verbose_name='Сфера Деятельности')
    telephone = models.CharField(max_length=20,blank=True, verbose_name='Телефон')
    email = models.EmailField(blank=True)
    feedback = models.TextField(null=True, blank=True, verbose_name="Отзывы и предложения")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fio

    class Meta:
        ordering = ('-created',)
        verbose_name='Выпускники'
        verbose_name_plural='Выпускники'


class Photo(models.Model):
    photo = models.ImageField(upload_to='images')

    class Meta:
        verbose_name='Фото'
        verbose_name_plural='Фото'


