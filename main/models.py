from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name