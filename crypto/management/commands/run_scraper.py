from django.core.management.base import BaseCommand
from crypto.views import create_data_excel


class Command(BaseCommand):
    help = 'This command create excel file of our db'

    def handle(self, *args, **options):
        create_data_excel()
