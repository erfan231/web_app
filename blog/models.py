from django.db import models
from django.db import connection
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

   
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})








