from django.db import models
from user_auth.models import Profile
from django.contrib.auth.models import User


class Sport(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField(max_length=1000, blank=True, null=True)
    winning_criteria = models.TextField(max_length=1000, blank=True, null=True)
    rules = models.TextField(max_length=1000, blank=True, null=True)
    objective = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class FavoriteSports(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('sport', 'user')

    def __str__(self):
        return self.sport


class Tournaments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name