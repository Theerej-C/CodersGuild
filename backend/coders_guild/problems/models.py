from django.db import models

class ProblemsModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=30)
    test_cases = models.TextField()
