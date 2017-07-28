from django.contrib import admin
from eajforms.forms.models import *

# Register your models here.

class AlternativeInline(admin.TabularInline):
    model = Alternative

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AlternativeInline]

admin.site.register(Form)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Alternative)
