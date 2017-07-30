from django.contrib import admin
from eajforms.forms.models import *

# Register your models here.

class AlternativeInline(admin.TabularInline):
    model = Alternative

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AlternativeInline]

class QuestionInline(admin.TabularInline):
    model = Question

class FormAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Alternative)
admin.site.register(Answer)
admin.site.register(AnswerOption)
admin.site.register(Response)
admin.site.register(ApplyForm)
