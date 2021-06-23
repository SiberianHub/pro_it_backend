from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=31)


class Skill(models.Model):
    level = models.IntegerField()
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)


class User(models.Model):
    FIO = models.CharField(max_length=127)
    skills = models.ManyToManyField(Skill)


class Team(models.Model):
    pass


class UserInTeam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=63)
    description = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
