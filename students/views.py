from django.views import View, generic
from django.http import JsonResponse, Http404
from django.db.models import Max, Avg

from .models import StudentMark
from .filters import StudentMarkFilter


class ColumnChartView(View):

    def get(self, request, *args, **kwargs):
        main_query = self.get_queryset()
        main_query = self.filter_queryset(main_query)
        avg_queryset = self.get_avg_queryset()
        avg_queryset = self.filter_queryset(avg_queryset)

        subjects, values, avg = self.format_data(main_query, avg_queryset)

        return JsonResponse({
            "subjects": subjects,
            "data": values,
            'avg': avg
        })

    def get_queryset(self):
        queryset = StudentMark.objects.values('subject')
        return queryset.annotate(value=Max('mark'))

    def get_avg_queryset(self):
        queryset = StudentMark.objects.values('subject')
        return queryset.annotate(avg=Avg('mark'))

    def filter_queryset(self, queryset):
        return StudentMarkFilter(
            data=self.request.GET,
            queryset=queryset
        ).qs

    def format_data(self, main_query, avg_queryset):
        chart_data = {}
        subjects = []
        values = []
        avg = []

        # add values
        for d in main_query:
            subject = d["subject"]
            value = d["value"]

            if subject not in chart_data:
                chart_data[subject] = {}

            chart_data[subject]["value"] = value

        # add marks
        for d in avg_queryset:
            subject = d["subject"]
            chart_data[subject]['avg'] = d["avg"]

        # format data
        for key, data in chart_data.items():
            subjects.append(key)
            values.append(data["value"])
            avg.append(data["avg"])

        return subjects, values, avg


class ChartsTemplateView(generic.TemplateView):

    templates = {
        "column-chart": "students/column_chart.html"
    }

    def get_template_names(self):
        type_of = self.kwargs.get("type_of")

        if type_of not in self.templates:
            raise Http404()

        return [self.templates[type_of]]
