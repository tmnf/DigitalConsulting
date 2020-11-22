from django.db import models


# Create your models here.

class Solution(models.Model):
    problem = models.CharField(max_length=30)
    variables = models.CharField(max_length=10000)

    def __str__(self):
        return self.problem + " " + str(self.id)
