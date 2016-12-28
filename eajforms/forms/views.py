from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def reply_form(request, formid):
    return render(request, 'form/form_reply.html')

def new(request):
    return render(request, 'form/form_form.html')
