import json
from django.shortcuts import render, redirect, get_object_or_404, resolve_url as r
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from .models import Form, Question, Alternative, Answer, AnswerOption, Response, ApplyForm
from eajforms.core.models import CoordinatorPole
from django.db import transaction


def reply_form(request, formid):
    return render(request, 'form/form_reply.html')


def form_new(request):
    return render(request, 'form/form_form.html')


def form_list(request):
    forms = Form.objects.all()
    return render(request, 'form/form_list.html', {"forms":forms})


def apply_form_list(request):
    apply_forms = ApplyForm.objects.all()
    return render(request, 'apply_form/apply_form_list.html', {"apply_forms":apply_forms})


def apply_form_result(request, access_code):
    apply_form = get_object_or_404(ApplyForm, access_code=access_code)

    return render(request, 'apply_form/apply_form_result.html', {"apply_form":apply_form})


def form_apply(request, pk):
    form = get_object_or_404(Form, pk=pk)

    coordinators_pole = CoordinatorPole.objects.filter(status=1)

    return render(request, 'form/form_apply.html', {"form":form, "coordinators_pole":coordinators_pole})


def form_response(request, access_code):
    apply_form = get_object_or_404(ApplyForm, access_code=access_code)
    form = apply_form.form

    return render(request, 'form/form_response.html', {"form":form, "apply_form":apply_form})


#@transaction.atomic
def form_response_save(request):
    form = Form.objects.get(pk=request.POST["form_id"])
    response = Response()
    response.apply_form = get_object_or_404(ApplyForm, access_code=request.POST["apply_form_access_code"])
    response.save()

    for question in form.question_set.all():
        
        if question.type_question == 1:
            answer = Answer()
            answer.question = question
            answer.response = response
            answer.text = request.POST["question_"+str(question.pk)]
            answer.save()
        elif question.type_question == 2:
            answer = Answer()
            answer.question = question
            answer.response = response
            answer.text = request.POST["question_"+str(question.pk)]
            answer.save()
        elif question.type_question == 3:
            option = request.POST["question_"+str(question.pk)]
            if option != "":
                alternative = Alternative.objects.get(pk=int(option))
                answerOption = AnswerOption()
                answerOption.question = question
                answerOption.response = response
                answerOption.option_choice = alternative
                answerOption.save()
        elif question.type_question == 4:
                try:
                    options = request.POST.getlist("question_"+str(question.pk))
                    for option in options:
                        alternative = Alternative.objects.get(pk=int(option))
                        answerOption = AnswerOption()
                        answerOption.question = question
                        answerOption.response = response
                        answerOption.option_choice = alternative
                        answerOption.save()                    
                except Exception as e:
                    pass
        elif question.type_question == 5:
            answer = Answer()
            answer.question = question
            answer.response = response
            try:
                not_apply = request.POST["not_apply_question_"+str(question.pk)]
                answer.not_apply = True
            except Exception as e:
                answer.scale = request.POST["question_"+str(question.pk)]
            answer.save()
        elif question.type_question == 6:
            try:
                answer = Answer()
                answer.question = question
                answer.response = response

                resp = request.POST["question_"+str(question.pk)]
 
                if resp == "not_apply":
                    answer.dont_apply = True
                else:
                    answer.yes_no = int(resp)  
                
                answer.save()
            except Exception as e:
                pass

    return render(request, 'form/finish_form_response.html')

#@transaction.atomic
@login_required
def form_save(request):
    if not request.is_ajax():
        raise Http404

    title = request.POST["title"]
    description = request.POST["description"]    
    questions = json.loads(request.POST["questions"])

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
                if alternative != "":
                    alternative = Alternative.objects.create(
                        title=alternative,
                        question=question
                        )
                
    response_data = {}
    response_data['result'] = 'success'
    response_data['message'] = 'O formulário foi cadastrado com sucesso!'
    response_data['pk'] = form.pk

    return JsonResponse(response_data)
