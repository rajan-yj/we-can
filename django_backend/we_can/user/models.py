from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100, primary_key=True)
  score = models.IntegerField(default=0)
  joined_at = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
      return self.name
