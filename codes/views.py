from django.shortcuts import render

from .models import Department, Subject, Practicle

def index(request):
    departments = Department.objects.all()

    context = {
        'departments' : departments,
    }

    return render(request, 'codes/homepage.html', context)


def detail_subject(request, subject_id):
    departments = Department.objects.all()
    subject = Subject.objects.get(id=subject_id)
    practicles = subject.practicle_set.all()

    context = {
        'departments' : departments,
        'subject' : subject,
        'practicles' : practicles,
    }

    return render(request, 'codes/detailsubject.html', context)

def detail_practicle(request, practicle_id):
    departments = Department.objects.all()
    practicle = Practicle.objects.get(id=practicle_id)
    subject = practicle.subject
    practicles = subject.practicle_set.all()

    context ={
        'departments' : departments,
        'practicle' : practicle,
        'subject' : subject,
        'practicles' : practicles,
    }

    return render(request, 'codes/detailpracticle.html', context)
