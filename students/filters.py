import django_filters

from .models import StudentMark
from .import constants


class StudentMarkFilter(django_filters.FilterSet):

    s_ids = dict(constants.STUDENTS_DATA).keys()
    student_id_choices = [(s, s) for s in s_ids]
    grade_choices = [(g, g) for g in constants.GRADES]
    year_choices = [(g, g) for g in constants.YEARS]
    subject_choices = [(s, s) for s in constants.SUBJECTS]

    student_id = django_filters.ChoiceFilter(choices=student_id_choices)
    year = django_filters.ChoiceFilter(choices=year_choices)
    grade = django_filters.ChoiceFilter(choices=grade_choices)
    subject = django_filters.ChoiceFilter(choices=subject_choices)

    class Meta:
        model = StudentMark
        fields = ['student_id', 'year', 'grade', 'subject']
