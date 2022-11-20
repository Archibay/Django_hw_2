from django.db import models


class Quote(models.Model):
    text = models.TextField()
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Author(models.Model):
    name = models.CharField(max_length=50)
    born_date = models.DateField()
    born_location = models.CharField(max_length=200)
    description = models.TextField()
    quotes = models.ManyToManyField(Quote)

    def __str__(self):
        return self.name
