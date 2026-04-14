import json

from django.core.management.base import BaseCommand
from datetime import date
from books.models import Book


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        with open('fixtures/books.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

            for rec in data:
                Book(
                    id=rec["pk"],
                    name=rec['fields']['name'],
                    author=rec['fields']['author'],
                    pub_date=date.fromisoformat(rec['fields']['pub_date'])
                ).save()

        self.stdout.write(f"Внесено {len(data)} записей")
