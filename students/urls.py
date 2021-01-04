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
        'charts/column-chart/data',
        views.ColumnChartView.as_view(),
        name="columns_chart"
    ),
]
