from django.contrib import admin

# Register your models here
from .models import *

admin.site.register(Candidates)
admin.site.register(Candidatesold)
admin.site.register(Homelanguages)
admin.site.register(Matricschools)
admin.site.register(Matricsubjects)
admin.site.register(Postgradqualifications)
admin.site.register(Postgraduniversities)
admin.site.register(Questions)
admin.site.register(Trainingelectives)
admin.site.register(Undergradqualifications)
admin.site.register(Undergraduniversities)
admin.site.register(QuestionnaireQuestion)
admin.site.register(TestModel)