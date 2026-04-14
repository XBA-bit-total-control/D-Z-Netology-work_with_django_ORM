import csv
import re

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            list_phones = list(csv.DictReader(file, delimiter=';'))

        for phone in list_phones:
            text = re.findall(r'\w+', phone['name'])

            slug = '_'.join([word.lower() for word in text])

            Phone.objects.create(
                id=phone['id'],
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=slug
            )