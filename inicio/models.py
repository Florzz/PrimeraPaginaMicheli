from django.db import models

class Painting(models.Model):
    artist = models.CharField(max_length=20) 
    style = models.CharField(max_length=20) 
    price = models.IntegerField(max_length=10)


    def __str__(self):
        return f'Painting ({self.id}): {self.artist}, {self.style}, {self.price}'