from django.db import models

# Create your models here.
class Formulario(models.Model):

    class Meta:
        verbose_name = "Formulário"
        verbose_name_plural = "Formulários"

    def __str__(self):
        pass

class Questao(models.Model):

    class Meta:
        verbose_name = "Questao"
        verbose_name_plural = "Questões"

    def __str__(self):
        pass

class Alternativa(models.Model):

    class Meta:
        verbose_name = "Alternativa"
        verbose_name_plural = "Alternativas"

    def __str__(self):
        pass

class TipoQuestao(models.Model):

    class Meta:
        verbose_name = "Tipo de Questões"
        verbose_name_plural = "Tipos de questões"

    def __str__(self):
        pass
    