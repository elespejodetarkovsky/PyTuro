from django.shortcuts import render
from .models import Project
from .models import Cursos
from .models import Inscripciones


def portfolio(request):
    projects = Project.objects.all()  # <=====
    return render(request, "portfolio/portfolio.html", {'projects':projects})

def cursos(request):
    listcursos = Cursos.objects.all()  # <=====
    return render(request, "portfolio/cursos.html", {'listcursos':listcursos})

def inscripciones(request):
    listCodi_cursos = Cursos.objects.values('id')
    listInscripciones = Inscripciones.objects.all()# <=====
    #listInscripciones = Inscripciones.objects.values_list('codi_curs',  flat=True)
    print(listCodi_cursos)
    print(listInscripciones)
    return render(request, "portfolio/inscripciones.html", {'listInscripciones':listInscripciones, 'listCodi_cursos':listCodi_cursos})