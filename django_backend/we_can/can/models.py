from statistics import mode
from django.db import models
from we_can.user.models import User

class Can(models.Model):
  name = models.CharField(max_length=100)
  location = models.JSONField()
  reported = models.BooleanField(default=False)
  joined_at = models.DateTimeField(auto_now_add=True, blank=True)

  def __str__(self):
      return self.name


class BinRequest(models.Model):
       location = models.JSONField()
       user = models.ForeignKey(to=User, on_delete=models.PROTECT)
       status = models.BooleanField(default=True)