from django.db import models
from eajforms.core.models import Person

# Create your models here.
class Form(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    DOCENTE = 1
    COORDINATOR = 2
    COURSE = 3
    POLE = 4
    TYPE_EVALUATED_CHOICE = (
        (DOCENTE,"Docente"),
        (COORDINATOR,"Coordenador"),
        (COURSE, "Curso"),
        (POLE, "Polo")

    )
    type_evaluated = models.PositiveIntegerField(choices=TYPE_EVALUATED_CHOICE)
    need_identify = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Formulário"
        verbose_name_plural = "Formulários"

    def __str__(self):
        pass

class Question(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    form = models.ForeignKey(Form)
    SHORT_TEXT = 1
    LONG_TEXT = 2
    UNIQUE_CHOICE = 3
    MULTIPLE_CHOICE = 4
    ESCALE = 5
    AGREE_DISAGREE = 6
    TYPE_QUESTION_CHOICES = (
        (SHORT_TEXT, "Texto Curto"),
        (LONG_TEXT, "Texto Longo"),
        (UNIQUE_CHOICE, "Escolha Única"),
        (MULTIPLE_CHOICE, "Escolha Múltipla"),
        (ESCALE, "Escala"),
        (AGREE_DISAGREE, "Concordo ou Discordo"),

    )

    type_question = models.PositiveIntegerField(choices = TYPE_QUESTION_CHOICES)
    is_required = models.BooleanField(default=True)
    related_alternative = models.ForeignKey('Alternative', null=True, related_name='related_alternative')

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"

    def __str__(self):
        pass

class Alternative(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    question = models.ForeignKey(Question)

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"

    def __str__(self):
        pass

class Answer(models.Model):
    text = models.CharField(max_length=255, null=True)
    option_choice = models.ForeignKey(Alternative, null=True)
    person = models.ForeignKey(Person, null=True)

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"

    def __str__(self):
        pass
    