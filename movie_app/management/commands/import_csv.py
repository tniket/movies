import csv
from django.core.management.base import BaseCommand
from movie_app.models import Movies
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='movies_app/movies.csv')

    def handle(self, *args, **options):
        with open(r'F:\movies_project\movie_app\movies.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row if present
            for row in csv_reader:
                # Assuming the date is in the second column (adjust as needed)
                original_date_str = row[1]
                try:
                    # Parse the date in its current format
                    original_date = datetime.strptime(original_date_str, '%Y-%m-%d')  # Adjust the format as needed
                    # Convert the date to the "YYYY-MM-DD" format
                    formatted_date_str = original_date.strftime('%Y-%m-%d')
                except ValueError:
                    formatted_date_str = None  # Handle invalid date format
                # Check if the date is valid or provide a default value
                if formatted_date_str:
                    Movies.objects.create(
                        title=row[0],
                        release_date=formatted_date_str,
                        genre=row[2],
                        director=row[3],
                        # Add other fields as needed
                    )
                else:
                    self.stdout.write(self.style.ERROR(f'Invalid date format in row: {row}'))
        self.stdout.write(self.style.SUCCESS('Successfully imported data from CSV.'))