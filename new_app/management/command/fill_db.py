from django.core.management.base import BaseCommand
from new_app.models import Author, Publisher, Book, Store
from faker import Faker
import random


fake = Faker()


class Command(BaseCommand):
    help = 'Fill db'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, choices=range(1, 101), help='Indicates the number of rows to be created')

    def handle(self, **kwargs):
        total = kwargs['total']
        objs = Author(name=fake.name(), age=random.randrange(20, 101))
        Author.objects.bulk_create(objs, total)
