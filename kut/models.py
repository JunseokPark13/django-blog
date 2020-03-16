from django.conf import settings
from django.db import models

# Create your models here.
class Problem(models.Model):
    prob_id = models.IntegerField(null=False)
    title = models.CharField(max_length=256)
    body_desc = models.TextField()
    input_desc = models.TextField()
    output_desc = models.TextField()
    time_limit = models.IntegerField(default=1)
    memory_limit = models.IntegerField(default=128)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
