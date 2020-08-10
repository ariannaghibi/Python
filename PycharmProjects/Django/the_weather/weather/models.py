from django.db import models


# create a table to store the city names in it
class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'

