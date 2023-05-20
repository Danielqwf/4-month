from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=112)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    type_book = models.TextField()
    genre = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
