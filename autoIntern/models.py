from django.db import models


class User(models.Model):
    email = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    displayName = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def getUserFromEmail(self, email):
        return User.objects.get(email=email)
