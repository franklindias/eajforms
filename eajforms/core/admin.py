from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Course)

class ClassCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_pole', 'start_at', 'end_at')

admin.site.register(ClassCourse, ClassCourseAdmin)
admin.site.register(Pole)
admin.site.register(Student)
admin.site.register(Docente)
admin.site.register(DocenteCoursePole)
admin.site.register(CoordinatorCourse)
admin.site.register(CoordinatorPole)

class CoursePoleAdmin(admin.ModelAdmin):
    list_display = ('course', 'pole')
    
admin.site.register(CoursePole, CoursePoleAdmin)

admin.site.register(Person)
admin.site.register(Matriculation)





