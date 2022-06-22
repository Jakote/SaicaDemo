from django.urls import path
from . import views

urlpatterns = [
    # path('', views.questionnaire, name='questionnaire'),
    path('', views.index, name='index'),
    path('questionnairep2', views.questionnairep2, name='questionnairep2'),
    path('questionnairep3', views.questionnairep3, name='questionnairep3'),
    path('questionnairep4', views.questionnairep4, name='questionnairep4'),
    path('questionnairep5', views.questionnairep5, name='questionnairep5'),
    path('questionnairep6', views.questionnairep6, name='questionnairep6'),
    path('questionnairep7', views.questionnairep7, name='questionnairep7'),
    path('questionnairep8', views.questionnairep8, name='questionnairep8'),
    path('questionnairep9', views.questionnairep9, name='questionnairep9'),
    path('questionnairep9', views.questionnairesubmitted, name='questionnairesubmitted'),
]