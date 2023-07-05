import csv

from django.core.management.base import BaseCommand
from django.test import Client


class Command(BaseCommand):
    help = 'Import player data from a CSV file using the API'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The name of the CSV file to import')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        self.import_data(csv_file)

    def import_data(self, csv_file):
        client = Client()
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Make a request to the API to insert the data
                response = client.post('/api/players/', data=row)
                if response.status_code == 201:
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported data: {row}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Failed to import data: {row}'))
                    self.stdout.write(self.style.ERROR(str(response.data)))
