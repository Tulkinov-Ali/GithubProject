from django.db import models


class GithubLogin(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.name

