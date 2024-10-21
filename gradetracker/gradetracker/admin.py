from django.contrib import admin
from .models import Course, Assignment, Grade
# admin can add course, assignmnet, and grade
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Grade)