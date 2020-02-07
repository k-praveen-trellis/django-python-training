from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    image = models.URLField(max_length=200)
    colors = ['green','red','orange','yellow','pink','blue']
    CHOICES = [
    ('green',colors[0]),
    ('red',colors[1]),
    ('orange',colors[2]),
    ('yellow',colors[3]),
    ('pink',colors[4]),
    ('blue',colors[5])
    ]
    color = models.CharField(max_length=50,choices=CHOICES,default='green')

    def __str__(self):
        return self.title
