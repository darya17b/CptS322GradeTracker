"""
This class serves as a database which shows the creation of 3 table
Course
Assignmnet
Grade
"""

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    """ 
    name : name of the course
    instructor : name of the instructor
    """
    name = models.CharField(max_length = 200)
    code = models.CharField(max_length = 5, unique=True)
    instructor = models.CharField(max_length = 200)

    def __str__(self):
        return f"{self.code}: {self.name}"

class Assignment(models.Model):
    """
    course: ForeignKey that link the assignmnet to the specific course
    title : the title of the assignment
    total_point : the total pint of an assignmnet that could have
    """
    course = models.ForeignKey(Course, on_delete= models.CASCADE)
    title = models.CharField(max_length = 200)
    total_points = models.IntegerField()

    def __str__(self):
        return self.title

class Grade(models.Model):
    """
    studnet: link the grade to the specific student 
    assignmnet: link the grade to the specific assignmnet
    score: the score a person got 
    feedback: this is anentry feedback that admin can write into it. 
    """
    student = models.ForeignKey(User, on_delete = models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete = models.CASCADE)
    score = models.IntegerField()
    feedback = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title}: {self.score}"
