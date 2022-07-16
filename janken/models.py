from django.db import models

# Create your model

class Janken(models.Model):
    user_name=models.CharField(max_length=20)
    win=models.IntegerField()

    def __str__(self):
        return self.user_name