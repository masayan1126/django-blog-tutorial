from django.db import models


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"
