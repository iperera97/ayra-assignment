from django.urls import path

from .views import ChartsTemplateView


app_name = "students"

urlpatterns = [
    path(
        'charts/<str:type_of>/',
        ChartsTemplateView.as_view(),
        name="charts_template"
    ),
]
