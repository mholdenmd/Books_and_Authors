from django.db import models
from django.db.models.base import Model

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Book object: {self.title} ({self.id})>"


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.ManyToManyField(Book, related_name="publishers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Author object: {self.first_name} {self.last_name}({self.id})>"