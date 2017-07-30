from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MatriculationsUploadFileForm
import json, csv, os, random
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from .models import ClassCourse, Student, Matriculation


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
    return render(request, 'class/class_list.html', {"class_list":class_list})

@login_required
def class_matriculations(request, pk):
    form = MatriculationsUploadFileForm()
    class_ = ClassCourse.objects.get(pk=pk)
    return render(request, 'class/class_matriculations.html', {"class":class_, "form":form})

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

def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)