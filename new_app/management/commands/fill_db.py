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
        for t in range(total_a):
            objs = Author(name=fake.name(), age=random.randrange(20, 101))
            objs.save()
        # Author.objects.bulk_create([
        #     Author(name=fake.name(), age=random.randrange(20, 101)),
        #     ], batch_size=total_a)

        # add Publishers
        total_p = kwargs['total_p']
        for t in range(total_p):
            objs = Publisher(name=fake.company())
            objs.save()
        # Publisher.objects.bulk_create([
        #     Publisher(name=fake.company()),
        # ], batch_size=total_p)

        # add Books
        total_b = kwargs['total_b']
        try:
            max_p = Publisher.objects.latest('id').id
        except ValueError:
            max_p = 1
        for i in range(total_b):
            random_publisher = random.randrange(1, max_p + 1)
            objs = Book(name=fake.word(),
                        pages=random.randrange(1, 1000),
                        price=random.randrange(1, 100),
                        rating=random.randrange(1, 11),
                        publisher=Publisher.objects.get(id=random_publisher),
                        pubdate=fake.date_between(start_date='-80y', end_date='today'))
            objs.save()
            try:
                max_a = Author.objects.latest('id').id
            except ValueError:
                max_a = 1
            for a in range(random.randrange(1, 4)):
                r_authors = Author.objects.get(id=random.randrange(1, Author.objects.latest('id').id)).id
                objs.authors.add(r_authors)

        # add Stores
        total_s = kwargs['total_s']
        for b in range(total_s):
            objs = Store(name=fake.company())
            objs.save()
            for a in range(random.randrange(1, 4)):
                r_books = Book.objects.get(id=random.randrange(1, Book.objects.latest('id').id)).id
                objs.books.add(r_books)
