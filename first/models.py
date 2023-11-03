from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50, null=True, blank=True)
    info = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='image', null=True, blank=True)
    janre = models.ForeignKey('Janre', on_delete=models.PROTECT, null=True, blank=True)
    author_book = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return f'{self.id} {self.author} {self.name}'


class Janre(models.Model):
    janre_book = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id} {self.janre_book}'


class Author(models.Model):
    author_book = models.CharField(max_length=25)

    def __str__(self):
        return self.author_book


class USD(models.Model):
    usd_now = models.FloatField()
    data = models.DateTimeField(auto_now=True)
