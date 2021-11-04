from django.db import models



# Create your models here.

class Temperature(models.Model):
    temperature = models.CharField(max_length=3)
    humidity = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.temperature