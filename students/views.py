from django.views import View, generic
from django.http import JsonResponse, Http404


class ColumnChartView(View):

    def get_queryset(self):
        pass

    def filter_queryset(self, queryset):
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset()

        return JsonResponse({
            "axis": self.get_axis(),
            "data": []
        })

    def get_axis(self):
        return {
            "x": ["maths", "english", "science", "accounting", "art", "it"],
            "y": 0
        }


class ChartsTemplateView(generic.TemplateView):

    templates = {
        "column-chart": "students/column_chart.html"
    }

    def get_template_names(self):
        type_of = self.kwargs.get("type_of")

        if type_of not in self.templates:
            raise Http404()

        return [self.templates[type_of]]
