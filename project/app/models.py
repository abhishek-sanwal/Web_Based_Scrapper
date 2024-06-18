from django.db import models

# Create your models here.


class Url(models.Model):

    url = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self) -> str:

        return f"The link is :{self.url}"

    def __repr__(self) -> str:

        return f"Url({self.url})"
