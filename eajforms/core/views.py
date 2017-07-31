from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import MatriculationsUploadFileForm, DocentesUploadFileForm
import json, csv, os, random
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from .models import ClassCourse, Student, Matriculation, Docente, Course, \
                    CoordinatorPole, CoordinatorCourse, DocenteCoursePole, Pole, Course
from django.http import JsonResponse, Http404
from django.core import serializers


def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def class_list(request):
    class_list = ClassCourse.objects.all()

    paginator = Paginator(class_list, 10)

    page = request.GET.get('page')
    try:
        class_list = paginator.page(page)
    except PageNotAnInteger:
        class_list = paginator.page(1)
    except EmptyPage:
        class_list = paginator.page(paginator.num_pages)

    return render(request, 'class/class_list.html', {"class_list":class_list})


@login_required
def course_list(request):
    course_list = Course.objects.all()

    paginator = Paginator(course_list, 10)

    page = request.GET.get('page')
    try:
        course_list = paginator.page(page)
    except PageNotAnInteger:
        course_list = paginator.page(1)
    except EmptyPage:
        course_list = paginator.page(paginator.num_pages)

    return render(request, 'course/course_list.html', {"course_list":course_list})


@login_required
def docente_list(request):
    form = DocentesUploadFileForm()

    docente_list = Docente.objects.all()

    paginator = Paginator(docente_list, 10)

    page = request.GET.get('page')
    try:
        docente_list = paginator.page(page)
    except PageNotAnInteger:
        docente_list = paginator.page(1)
    except EmptyPage:
        docente_list = paginator.page(paginator.num_pages)

    return render(request, 'docente/docente_list.html', {"docente_list":docente_list, "form":form})

@login_required
@transaction.atomic
def docente_upload(request):
    if request.method == "POST":
        form = DocentesUploadFileForm(request.POST, request.FILES)
            
        if form.is_valid():
            filehandle = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(filehandle.name, filehandle)
            uploaded_file_url = fs.url(filename)

            with open(settings.BASE_DIR + "/" + uploaded_file_url, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row["NOME"].strip()
                    first_name = row["NOME"].strip().split(" ")[0]
                    cpf = row["CPF"].strip()
                    email = row["EMAIL"].strip()

                    docente = Docente.objects.filter(cpf=cpf)

                    if not docente:
                        docente = Docente.objects.create(
                            full_name=name,
                            username=first_name+str(random.randint(9, 99999)),
                            cpf=cpf,
                            email=email
                            )

        _delete_file(settings.BASE_DIR + "/" + uploaded_file_url)

        return redirect('docente_list')


@login_required
def class_matriculations(request, pk):
    form = MatriculationsUploadFileForm()
    class_ = ClassCourse.objects.get(pk=pk)
    return render(request, 'class/class_matriculations.html', {"class":class_, "form":form})

@login_required
@transaction.atomic
def class_matriculation_upload(request):
    if request.method == "POST":
        form = MatriculationsUploadFileForm(request.POST, request.FILES)
            
        if form.is_valid():
            filehandle = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(filehandle.name, filehandle)
            uploaded_file_url = fs.url(filename)

            class_course = ClassCourse.objects.get(pk=int(request.POST['class_course_id']))

            with open(settings.BASE_DIR + "/" + uploaded_file_url, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row["NOME"].strip()
                    first_name = row["NOME"].strip().split(" ")[0]
                    cpf = row["CPF"].strip()
                    email = row["EMAIL"].strip()

                    student = Student.objects.filter(cpf=cpf)

                    if not student:
                        student = Student.objects.create(
                            full_name=name,
                            username=first_name+str(random.randint(9, 99999)),
                            cpf=cpf,
                            email=email
                            )
                    else:
                        student = student[0]

                    matriculation = Matriculation.objects.filter(student=student, class_course=class_course)

                    if not matriculation:
                        matriculation = Matriculation.objects.create(
                            student=student,
                            class_course=class_course
                            )
                    else:
                        matriculation[0].situation = 1
                        matriculation[0].save()
        else:
            pass

        _delete_file(settings.BASE_DIR + "/" + uploaded_file_url)

        class_ = ClassCourse.objects.get(pk=int(request.POST['class_course_id']))
        return render(request, 'class/class_matriculations.html', {"class":class_, "form":form})


@login_required
def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


@login_required
def load_avaluated_by_type(request):
    if not request.is_ajax():
        raise Http404

    type_evaluated = int(request.POST['type'])

    list_data = []

    if type_evaluated == 1:
        coordinators_pole = CoordinatorPole.objects.filter(status=1)
        for cp in coordinators_pole:
            list_data.append({
                "value":cp.pk,
                "display":cp.pole.name + " - " + cp.docente.full_name
            })
    elif type_evaluated == 2:
        coordinators_course = CoordinatorCourse.objects.filter(status=1)
        for cc in coordinators_course:
            list_data.append({
                "value":cc.pk,
                "display":cc.course.name + " - " + cc.docente.full_name
            })
    elif type_evaluated == 3 or type_evaluated == 4 or type_evaluated == 5 or type_evaluated == 6 or type_evaluated == 7:
        docente_course_pole = DocenteCoursePole.objects.filter(status=1, type_docente=type_evaluated-2)
        for dcp in docente_course_pole:
            list_data.append({
                "value":dcp.pk,
                "display":dcp.course_pole.pole.name + " | " + dcp.course_pole.course.name + " - " + dcp.docente.full_name
            })
    elif type_evaluated == 8:
        course_list = Course.objects.all()
        for c in course_list:
            list_data.append({
                "value":c.pk,
                "display":c.name
            })
    elif type_evaluated == 9:
        pole_list = Pole.objects.all()
        for p in pole_list:
            list_data.append({
                "value":p.pk,
                "display":p.name
            })

    return JsonResponse(list_data, safe=False)