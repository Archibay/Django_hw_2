from django.core.management.base import BaseCommand
from new_app.models import Author, Publisher, Book, Store
from faker import Faker
import random


fake = Faker()


class Command(BaseCommand):
    help = 'Fill db'

    def add_arguments(self, parser):
        parser.add_argument('total_a', type=int, choices=range(0, 101), help='Numbers of Authors')
        parser.add_argument('total_p', type=int, choices=range(0, 101), help='Numbers of Publishers')
        parser.add_argument('total_b', type=int, choices=range(0, 101), help='Numbers of Books')
        parser.add_argument('total_s', type=int, choices=range(0, 101), help='Numbers of Stores')

    def handle(self, **kwargs):
        # add Authors
        total_a = kwargs['total_a']
        Author.objects.bulk_create(
            [Author(name=fake.name(), age=random.randrange(20, 101)) for i in range(total_a)]
        )

        # add Publishers
        total_p = kwargs['total_p']
        Publisher.objects.bulk_create(
            [Publisher(name=fake.company()) for i in range(total_p)]
        )

        # add Books
        total_b = kwargs['total_b']
        p_list = Publisher.objects.values_list('id', flat=True)
        a_list = Author.objects.values_list('id', flat=True)
        for i in range(total_b):
            random_p = random.choice(p_list)
            objs = Book(name=fake.word(),
                        pages=random.randrange(1, 1000),
                        price=random.randrange(1, 100),
                        rating=random.randrange(1, 11),
                        publisher=Publisher.objects.get(id=random_p),
                        pubdate=fake.date_between(start_date='-80y', end_date='today'))
            objs.save()
            for a in range(random.randrange(1, 4)):
                random_a = random.choice(a_list)
                objs.authors.add(random_a)

        # add Stores
        total_s = kwargs['total_s']
        b_list = Book.objects.values_list('id', flat=True)
        for b in range(total_s):
            objs = Store(name=fake.company())
            objs.save()
            for a in range(random.randrange(1, 4)):
                random_b = random.choice(b_list)
                objs.books.add(random_b)
