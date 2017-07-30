from django.db import models
from eajforms.core.models import Person

# Create your models here.
class Form(models.Model):
    title = models.CharField('Título', max_length=100)
    description = models.TextField('Descrição', max_length=255)
    create_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    class Meta:
        verbose_name = "Formulário"
        verbose_name_plural = "Formulários"

    def __str__(self):
        return self.title

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
    related_alternative = models.ForeignKey('Alternative', null=True, blank=True, related_name='related_alternative')
    max_size = models.PositiveIntegerField('Tamanho máximo da resposta', null=True)
    max_scale = models.PositiveIntegerField('Escala máxima da resposta', null=True)
    show_yes_no = models.BooleanField('Mostrar Sim ou Não', default=False)
    left_label = models.CharField('Label esquerdo', max_length=50)
    middle_label = models.CharField('Label central', max_length=50)
    right_label = models.CharField('Label direito', max_length=50)

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"

    def __str__(self):
        return self.title

class Alternative(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True, blank=True)
    question = models.ForeignKey(Question)

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"

    def __str__(self):
        return self.title


class Response(models.Model):
    person = models.ForeignKey(Person, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    apply_form = models.ForeignKey("ApplyForm", default=1)
    
    class Meta:
        verbose_name = "Resposta Central"
        verbose_name_plural = "Respostas Central"

    def __str__(self):
        return str(self.create_at)


class Answer(models.Model):
    response = models.ForeignKey(Response, null=True)
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=255, null=True)
    scale = models.PositiveIntegerField(null=True)
    dont_apply = models.BooleanField('Não se aplica', default=False)
    OPTION_CHOICES = (
        (1, "Concordo/Sim"),
        (2, "Concordo parcialmente/Parcialmente"),
        (3, "Discordo/Não"),

    )
    yes_no = models.PositiveIntegerField(choices = OPTION_CHOICES, null=True, blank=True)

    class Meta:
        verbose_name = "Resposta"
        verbose_name_plural = "Respostas"

    def __str__(self):
        return str(self.question.title) + " - " + str(self.text) + "Null"

class AnswerOption(models.Model):
    question = models.ForeignKey(Question)
    response = models.ForeignKey(Response)
    option_choice = models.ForeignKey(Alternative, null=True, blank=True)

    class Meta:
        verbose_name = "Alternativa selecionada"
        verbose_name_plural = "Alternativa selecionada"

    def __str__(self):
        return self.question.title + " / " + self.option_choice.title


class ApplyForm(models.Model):
    form = models.ForeignKey(Form)
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
    type_evaluated = models.PositiveIntegerField('Tipo de Avaliado',choices=TYPE_EVALUATED_CHOICE)
    login_required = models.BooleanField('Login é obrigatório?', default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    access_code = models.CharField('código de acesso', unique=True, max_length=64)
    OPEN = 1
    CLOSE = 2
    STATUS_FORM_CHOICES = (
        (OPEN, "Aberto"),
        (CLOSE, "Fechado"),
    )
    status = models.PositiveIntegerField(choices = STATUS_FORM_CHOICES, default=1)

    class Meta:
        verbose_name = "Formulário Aplicado"
        verbose_name_plural = "Formulários Aplicados"

    def __str__(self):
        return self.form.title