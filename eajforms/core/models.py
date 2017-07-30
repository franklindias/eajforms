from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(User):
    cpf = models.CharField(max_length=12, null=True)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        pass

class Docente(Person):
    TEACHER = 1
    SEARCH_TEACHER = 2
    MEDIATOR_TEACHER = 3
    TUTOR = 4
    DISTANCE_TUTOR = 5
    TYPE_DOCENTE_CHOICE = (
        (TEACHER, "Professor"),
        (SEARCH_TEACHER, "Professor Pesquisador"),
        (MEDIATOR_TEACHER, "Professor Mediador"),
        (TUTOR, "Tutor Presencial"),
        (DISTANCE_TUTOR, "Tutor EAD"),

    )
    type_docente = models.PositiveIntegerField(choices=TYPE_DOCENTE_CHOICE)

    class Meta:
        verbose_name = "docente"
        verbose_name_plural = "docentes"

    def __str__(self):
        pass

class DocenteCoursePole(models.Model):
    course_pole = models.ForeignKey('CoursePole')
    docente = models.ForeignKey('Docente')
    create_at = models.DateField(auto_now_add=True)
    STATUS_CHOICES = (
        (1, "Ativado"),
        (2, "Desativado")
        )
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Docente em um curso"
        verbose_name_plural = "Docentes em um curso"

    def __str__(self):
        return self.docente.name

class Coordinator(Person):

    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def __str__(self):
        pass

class Pole(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Polo"
        verbose_name_plural = "Polos"

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.name

class ClassCourse(models.Model):
    course = models.ForeignKey(Course)
    pole = models.ForeignKey(Pole)
    start_at = models.DateField(auto_now=False, auto_now_add=False)
    end_at = models.DateField(auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

    def __str__(self):
        return self.course.name + " - " + str(self.start_at)


class Matriculation(models.Model):
    course_pole = models.ForeignKey('CoursePole')
    student = models.ForeignKey('Student')
    matriculation = models.CharField(max_length=30, null=True, blank=True)
    REGISTERED = 1
    RETIRED = 2
    LOCKED = 3
    FINISHED = 4
    SITUATION_CHOICES = (
        (REGISTERED, "Matriculado"),
        (RETIRED, "Jubilado"),
        (LOCKED, "Trancado"),
        (FINISHED, "Finalizado")
        )
    situation = models.PositiveIntegerField('Situação da Matrícula',choices=SITUATION_CHOICES, default=1)


class Student(Person):
    is_egress = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def __str__(self):
        return self.name


class CoursePole(models.Model):
    course = models.ForeignKey(Course)
    pole = models.ForeignKey(Pole)

    class Meta:
        verbose_name = "Curso do Polo"
        verbose_name_plural = "Cursos do Polo"

    def __str__(self):
        return self.course.name + " - " + self.pole.name


class CoordinatorCourse(models.Model):
    course = models.ForeignKey(Course)
    coordinator = models.ForeignKey(Coordinator)
    STATUS_CHOICES = (
        (1, "Ativado"),
        (2, "Desativado")
        )
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Coordenador de Curso"
        verbose_name_plural = "Coordenadores de Curso"

    def __str__(self):
        pass

class CoordinatorPole(models.Model):
    pole = models.ForeignKey(Pole)
    coordinator = models.ForeignKey(Coordinator)
    STATUS_CHOICES = (
        (1, "Ativado"),
        (2, "Desativado")
        )
    status = models.PositiveIntegerField(choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "Coordenador de Polo"
        verbose_name_plural = "Coordenadores de Polo"

    def __str__(self):
        pass
