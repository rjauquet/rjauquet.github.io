from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models

class Blog(models.Model):

    title = models.TextField()
    text = models.TextField()

    title_vector = SearchVectorField(null=True)
    text_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=[
            'text_vector',
            'title_vector',
        ])]
