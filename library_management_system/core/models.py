from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author, related_name="authors")
    genre = models.ManyToManyField(Genre, related_name="genres")
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title