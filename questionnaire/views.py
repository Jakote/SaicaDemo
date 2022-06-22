from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request, 'ModalCheck.html')

# def questionnaire(request):
    
#     candidates = Candidates.objects.all()
#     oldCandidates = Candidatesold.objects.all()
#     languages = Homelanguages.objects.all()
#     matricSchools = Matricschools.objects.all()
#     matricSubjects = Matricsubjects.objects.all()
#     postGradQualifications = Postgradqualifications.objects.all()
#     postGradUniverisities= Postgraduniversities.objects.all()
#     questions = Questions.objects.all().order_by('id').values()
#     trainingElectives = Trainingelectives.objects.all()
#     undergradQualifications = Undergradqualifications.objects.all()
#     undergradUniversities = Undergraduniversities.objects.all()
    
#     context={ "languages":languages,
#     "matricSchools":matricSchools,
#     "matricSubjects":matricSubjects,
#     "postGradQualifications":postGradQualifications, 
#     "postGradUniverisities":postGradUniverisities,
#     "questions":questions,"trainingElectives":trainingElectives, 
#     "undergradQualifications":undergradQualifications,
#     "undergradUniversities":undergradUniversities,
#     "questions":questions}

#     return render(request, 'QuestionnaireP2.html', context)

# def questionnaire(request):
#     data=request.POST.get('name')
#     rows = request.POST.get('table')
#     return render(request, 'test.html', {'data':data, 'rows': rows})

def questionnaire(request):
    return render(request, 'Questionnaire.html')

def questionnairep2(request):
    languages = Homelanguages.objects.all()
    context = {'languages':languages}
    return render(request, 'QuestionnaireP2.html', context)

def questionnairep3(request):
    matricSchools = Matricschools.objects.all()
    languages = Homelanguages.objects.all()
    return render(request, 'QuestionnaireP3.html', {'matricSchools':matricSchools, 'languages':languages})

def questionnairep4(request):
    matricSubjects = Matricsubjects.objects.all()
    tablerows = Table.objects.all()
    context  = {
        'tablerows': tablerows,
        'test': 3,
        'matricSubjects':matricSubjects,
    }
    return render(request, 'QuestionnaireP4.html', context)

def questionnairep5(request):
    undergradQualifications = Undergradqualifications.objects.all()
    undergradUniversities = Undergraduniversities.objects.all()
    return render(request, 'QuestionnaireP5.html', {'undergradQualifications': undergradQualifications,'undergradUniversities':undergradUniversities})

def questionnairep6(request):
    return render(request, 'QuestionnaireP6.html')

def questionnairep7(request):
    return render(request, 'QuestionnaireP7.html')

def questionnairep8(request):
    return render(request, 'QuestionnaireP8.html')

def questionnairep9(request):
    return render(request, 'QuestionnaireP9.html')

def questionnairesubmitted(request):
    return render(request, 'QuestionnaireSubmitted.html')
