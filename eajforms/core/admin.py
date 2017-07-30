from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Course)
admin.site.register(ClassCourse)
admin.site.register(Pole)
admin.site.register(Student)
admin.site.register(Docente)

