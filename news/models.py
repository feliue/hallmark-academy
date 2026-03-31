from django.db import models

# Create your models here.
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news/', blank=True)

    def __str__(self):
        return self.title
