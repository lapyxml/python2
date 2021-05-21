from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    title = models.CharField(
                            max_length=50,
                            db_index=True,
                            verbose_name="название комнаты")
    profile = models.TextField()
    designer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

