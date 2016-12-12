from django.db import models

# Create your models here.
class Pessoa(models.Model):
	
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        pass

class Docente(models.Model):

    class Meta:
        verbose_name = "docente"
        verbose_name_plural = "docentes"

    def __str__(self):
        pass
    
class Coordenador(models.Model):

    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def __str__(self):
        pass
    
class Egresso(models.Model):

    class Meta:
        verbose_name = "Egresso"
        verbose_name_plural = "Egressos"

    def __str__(self):
        pass
    

class Polo(models.Model):

    class Meta:
        verbose_name = "Polo"
        verbose_name_plural = "Polos"

    def __str__(self):
        pass

class Curso(models.Model):

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        pass
    

class CoordenadorCurso(models.Model):

    class Meta:
        verbose_name = "Coordenador de Curso"
        verbose_name_plural = "Coordenadores de Curso"

    def __str__(self):
        pass

class CoordenadorPolo(models.Model):

    class Meta:
        verbose_name = "Coordenador de Polo"
        verbose_name_plural = "Coordenadores de Polo"

    def __str__(self):
        pass