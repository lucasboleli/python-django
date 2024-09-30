from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
