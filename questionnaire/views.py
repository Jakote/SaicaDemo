from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def questionnaire(request):
    
    candidates = Candidates.objects.all()
    oldCandidates = Candidatesold.objects.all()
    languages = Homelanguages.objects.all()
    matricSchools = Matricschools.objects.all()
    matricSubjects = Matricsubjects.objects.all()
    postGradQualifications = Postgradqualifications.objects.all()
    postGradUniverisities= Postgraduniversities.objects.all()
    questions = Questions.objects.all().order_by('id').values()
    trainingElectives = Trainingelectives.objects.all()
    undergradQualifications = Undergradqualifications.objects.all()
    undergradUniversities = Undergraduniversities.objects.all()
    
    context={ "languages":languages,
    "matricSchools":matricSchools,
    "matricSubjects":matricSubjects,
    "postGradQualifications":postGradQualifications, 
    "postGradUniverisities":postGradUniverisities,
    "questions":questions,"trainingElectives":trainingElectives, 
    "undergradQualifications":undergradQualifications,
    "undergradUniversities":undergradUniversities,
    "questions":questions}

    return render(request, 'QuestionnaireP2.html', context)
