import random
from cProfile import Profile

from django.core.management.base import BaseCommand

from faker import Faker

from students.models import StudentMark


class Command(BaseCommand):

    help = 'add student records to the database'
    student_ids = list(range(100, 120))
    grades = list(range(1, 13))
    years = list(range(2010, 2020))
    marks = list(range(0, 101))
    subjects = ["maths", "english", "science", "accounting", "art", "it"]
    semesters = [1, 2]
    total_records = 10_000_000
    records_for_each_student = total_records // len(student_ids)
    max_objects_per_query = 100_000
    faker = Faker()

    def handle(self, *args, **options):
        """ entry point of the command """
        profiler = Profile()
        profiler.runcall(self._store_data, *args, **options)
        profiler.print_stats()

    def _store_data(self, *args, **options):
        """ create student mark objects in database """
        for s_id in self.student_ids:
            try:
                data_generator = self._get_objects(s_id)
                while True:
                    student_objects = next(data_generator)
                    StudentMark.objects.bulk_create(student_objects)
            except StopIteration:
                pass

    def _get_objects(self, student_id):
        """ get student objects

        Args:
            student_id (int)

        Yields:
            list: list of student objects
        """
        counter = 0
        returndata = []

        for n in range(self.records_for_each_student):
            s_obj = StudentMark(
                student_id=student_id,
                student_name=self.faker.name(),
                grade=random.choice(self.grades),
                subject=random.choice(self.subjects),
                year=random.choice(self.years),
                semester=random.choice(self.semesters),
                mark=random.choice(self.marks),
            )
            returndata.append(s_obj)
            counter += 1

            if counter == self.max_objects_per_query:
                yield returndata

                # reset data
                counter = 0
                returndata = []

        # if less than counter
        if returndata:
            yield returndata
