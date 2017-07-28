import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from .models import Form, Question, Alternative


def reply_form(request, formid):
    return render(request, 'form/form_reply.html')

def form_new(request):
    return render(request, 'form/form_form.html')

def form_list(request):
    forms = Form.objects.all()
    return render(request, 'form/form_list.html', {"forms":forms})

def form_apply(request, pk):
    form = Form.objects.get(pk=pk)
    return render(request, 'form/form_apply.html', {"form":form})

def form_response(request, code):
    form = Form.objects.get(pk=code)
    return render(request, 'form/form_response.html', {"form":form})

def form_save(request):
    if not request.is_ajax():
        raise Http404

    title = request.POST["title"]
    description = request.POST["description"]    
    questions = json.loads(request.POST["questions"])

    print (questions)

    form = Form.objects.create(
        title=title,
        description=description
        )

    for item in questions:
        
        question = Question.objects.create(
            title=item["question"],
            description=item["description"],
            form=form,
            type_question=item["type"],
            is_required=item["is_required"],
            max_size=item["max_characters"],
            max_scale=item["max_rating"],
            show_yes_no=item["show_yes_no"],
            left_label=item["label_left"],
            middle_label=item["label_middle"],
            right_label=item["label_right"]
            )

        if question.type_question == 3 or question.type_question == 4:
            for alternative in item["choices"].split("\n"):
                alternative = Alternative.objects.create(
                    title=alternative,
                    question=question
                    )
                
    response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = 'O formulário foi cadastrado com sucesso!'
    response_data['pk'] = form.pk

    return JsonResponse(response_data)
