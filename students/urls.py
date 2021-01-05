from django.urls import path

from .import views


app_name = "students"

urlpatterns = [
    path(
        'charts/<str:type_of>/',
        views.ChartsTemplateView.as_view(),
        name="charts_template"
    ),

    path(
        'charts/subject-marks/data',
        views.SubjectMarksView.as_view(),
        name="subject_marks"
    ),
    path(
        'charts/subject-progress/data',
        views.SubjectProgressChartView.as_view(),
        name="subject_progress"
    ),
]
