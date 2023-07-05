from django.db import models


class Player(models.Model):
    playerID = models.CharField(max_length=9, unique=True)
    birthYear = models.IntegerField(null=True, blank=True)
    birthMonth = models.IntegerField(null=True, blank=True)
    birthDay = models.IntegerField(null=True, blank=True)
    birthCountry = models.CharField(max_length=200, null=True, blank=True)
    birthState = models.CharField(max_length=200, null=True, blank=True)
    birthCity = models.CharField(max_length=200, null=True, blank=True)
    deathYear = models.IntegerField(null=True, blank=True)
    deathMonth = models.IntegerField(null=True, blank=True)
    deathDay = models.IntegerField(null=True, blank=True)
    deathCountry = models.CharField(max_length=200, null=True, blank=True)
    deathState = models.CharField(max_length=200, null=True, blank=True)
    deathCity = models.CharField(max_length=200, null=True, blank=True)
    nameFirst = models.CharField(max_length=200, null=True, blank=True)
    nameLast = models.CharField(max_length=200)
    nameGiven = models.CharField(max_length=200, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    bats = models.CharField(max_length=1, null=True, blank=True)
    throws = models.CharField(max_length=1, null=True, blank=True)
    debut = models.DateField(null=True, blank=True)
    finalGame = models.DateField(null=True, blank=True)
    retroID = models.CharField(max_length=9, null=True, blank=True)
    bbrefID = models.CharField(max_length=9, null=True, blank=True)

    class Meta:
        ordering = ['playerID']

