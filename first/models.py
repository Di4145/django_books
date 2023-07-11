from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    info = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='image', null=True, blank=True)

    def __str__(self):
        return f'{self.id} {self.author} {self.name}'
