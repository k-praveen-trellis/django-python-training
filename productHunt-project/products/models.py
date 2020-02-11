from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/',default='')
    votes_count = models.IntegerField(default=1)
    main_user_hunter = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
