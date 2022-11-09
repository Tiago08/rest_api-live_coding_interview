import names
import random_address
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from showdata.models import ShowData

class Command(BaseCommand):
    help = "Create Data"

    def add_arguments(self, parser):
        parser.add_argument("number", nargs='+', type=str)

    def handle(self, *args, **options):
        ShowData.objects.all().delete()
        for i in range(1, int(options['number'][0])):
            ShowData.objects.create(name=names.get_full_name(), address=random_address.real_random_address_by_state('CA')['city'])
            print("Data Created Successfully")