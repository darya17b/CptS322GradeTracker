from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grade  # Make sure Grade is correctly imported

# Define the student_grades view
@login_required
def student_grades(request):
    # Fetch the grades for the logged-in user
    grades = Grade.objects.filter(student=request.user)
    # Render the grades.html template with the fetched grades
    return render(request, 'gradetracker/grades.html', {'grades': grades})
