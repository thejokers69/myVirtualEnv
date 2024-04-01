# program/admin.py

from django.contrib import admin
from .models import Program, RegistersFor

admin.site.register(Program)
admin.site.register(RegistersFor)
