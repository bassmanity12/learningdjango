from django.db import models

# Create your models here.
from datetime import datetime

class Todo(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title

