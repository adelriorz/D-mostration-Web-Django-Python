import csv
from datetime import datetime
from demo.models import DataPoint
from django.conf import settings
try:
    from django.core.management.base import NoArgsCommand as BaseCommand
except ImportError:
    from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Load data from CSV file"
    
    def handle(self, *args, **kwargs):
        
        file_path = settings.BASE_DIR / 'data' / 'Example - Data.csv'
            
        with open(file_path, 'r', newline='') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)

            # Skip the header row
            next(csv_reader)

            # Iterate over the remaining rows
            for row in csv_reader:
                # Convert the date string to a datetime object
                date = datetime.strptime(row[0], '%Y-%m-%d').date()

                # Create a DataPoint instance
                data_point = DataPoint(date=date, value=int(row[1]))

                # Save the instance to the database
                data_point.save()
