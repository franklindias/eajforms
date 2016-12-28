from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(User):
    cpf = models.CharField(max_length=12)
    matriculation_number = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        pass

class Docente(Person):
    TEACHER = 1
    DISTANCE_TEACHER = 2
    MEDIATOR = 3
    TUTOR = 4
    TYPE_DOCENTE_CHOICE = (
        (TEACHER, "Professor"),
        (DISTANCE_TEACHER, "Professor à Distância"),
        (MEDIATOR, "Mediador"),
        (TUTOR, "Tutor"),

    )
    type_docente = models.PositiveIntegerField(choices=TYPE_DOCENTE_CHOICE)

    class Meta:
        verbose_name = "docente"
        verbose_name_plural = "docentes"

    def __str__(self):
        pass

class Coordinator(Person):

    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def __str__(self):
        pass

class Pole(models.Model):

    class Meta:
        verbose_name = "Polo"
        verbose_name_plural = "Polos"

    def __str__(self):
        pass

class Course(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        pass

class Student(Person):
    is_egress = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        pass

class StudentCourse(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    year_started = models.IntegerField()
    year_finish = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Aluno do Curso"
        verbose_name_plural = "Alunos do Curso"

    def __str__(self):
        pass


class CoursePole(models.Model):
    course = models.ForeignKey(Course)
    pole = models.ForeignKey(Pole)

    class Meta:
        verbose_name = "Curso do Polo"
        verbose_name_plural = "Cursos do Polo"

    def __str__(self):
        pass

class CoordinatorCourse(models.Model):
    course = models.ForeignKey(Course)
    coordinator = models.ForeignKey(Coordinator)

    class Meta:
        verbose_name = "Coordenador de Curso"
        verbose_name_plural = "Coordenadores de Curso"

    def __str__(self):
        pass

class CoordinatorPole(models.Model):
    pole = models.ForeignKey(Pole)
    coordinator = models.ForeignKey(Coordinator)

    class Meta:
        verbose_name = "Coordenador de Polo"
        verbose_name_plural = "Coordenadores de Polo"

    def __str__(self):
        pass
