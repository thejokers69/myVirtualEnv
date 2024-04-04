from django.contrib import admin
from .models import Program, Subject, ProgramSubject

# Register your models here.
admin.site.register(Program)
admin.site.register(Subject)
admin.site.register(ProgramSubject)