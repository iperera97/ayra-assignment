import random
import time

from django.core.management.base import BaseCommand

from students.models import StudentMark
from students import constants


class Command(BaseCommand):

    help = 'add student records to the database'
    students_data = dict(constants.STUDENTS_DATA)
    student_ids = students_data.keys()
    grades = list(range(1, 13))
    years = list(range(2010, 2020))
    marks = list(range(0, 101))
    subjects = ["maths", "english", "science", "accounting", "art", "it"]
    semesters = [1, 2]
    total_records = 10_000_000
    records_for_each_student = total_records // len(student_ids)
    max_objects_per_query = 10_000

    def handle(self, *args, **options):
        """ create student mark objects in database """

        for s_id in self.student_ids:
            self.stdout.write(self.style.SUCCESS(f'starting for {s_id}'))

            try:
                data_generator = self._get_objects(s_id)
                while True:
                    student_objects = next(data_generator)
                    StudentMark.objects.bulk_create(student_objects)
            except StopIteration:
                self.stdout.write(self.style.SUCCESS(f'records added {s_id}'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS(f'{self.total_records} records added'))  # noqa

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
                student_name=self.students_data[student_id],
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
