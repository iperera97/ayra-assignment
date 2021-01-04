from django.db import models


class StudentMark(models.Model):

    student_id = models.PositiveIntegerField()
    student_name = models.CharField(max_length=64)
    grade = models.CharField(max_length=32)
    subject = models.CharField(max_length=64)
    year = models.PositiveSmallIntegerField()
    semester = models.PositiveSmallIntegerField()
    mark = models.CharField(max_length=16)

    def __str__(self):
        return f"#{self.student_id} mark"
