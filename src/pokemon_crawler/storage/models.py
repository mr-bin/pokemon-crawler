from django.db import models


class Ability(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Form(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Move(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Stat(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Type(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    weight = models.IntegerField()

    description = models.CharField(max_length=30)

    abilities = models.ManyToManyField(Ability)
    forms = models.ManyToManyField(Form)
    moves = models.ManyToManyField(Move)
    stats = models.ManyToManyField(Stat)
    types = models.ManyToManyField(Type)
