from django.core.management.base import BaseCommand

from students.models import StudentMark


class Command(BaseCommand):

    help = 'delete all student records in the database'

    def handle(self, *args, **options):
        StudentMark.objects.all().delete()
