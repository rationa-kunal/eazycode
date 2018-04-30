from django.shortcuts import render

from .models import Department, Subject, Practicle

def index(request):
    departments = Department.objects.all()

    context = {
        'departments' : departments,
    }

    return render(request, 'codes/index.html', context)


def view_codes(request, depart_id, subject_id, practicle_id):
    departments = Department.objects.all()
    sub = Subject.objects.get(id=subject_id)
    sub_practicles = sub.practicle_set.all()
    pract = Practicle.objects.get(id=practicle_id)

    context = {
        'departments' : departments,
        'sub_practicles' : sub_practicles,
        'sub' : sub,
        'pract' : pract,
    }

    return render(request, 'codes/base.html', context)

def view_pre_codes(request, depart_id, subject_id):
    pract = Subject.objects.get(id=subject_id).practicle_set.all()
    pract = pract[0]
    return view_codes(request, depart_id, subject_id, pract.id)
