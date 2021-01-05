from django.shortcuts import redirect


def home(request):
    pattern = "students:charts_template"
    type_of = "subject-marks"
    return redirect(pattern, type_of=type_of)
