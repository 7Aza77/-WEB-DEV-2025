from django.db import models

class Student():
    name = models.CharField(max_length=150)
    scores = models.JSONField()

    def get_average_score(self):
        sum =0
        arr = [self.scores]
        return sum(self.scores) / len(arr)

    def get_top_score(self):
        return max(self.scores)

# Create your models here.
