from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    title = models.CharField(
                            max_length=50,
                            db_index=True,
                            verbose_name="название комнаты")
    profile = models.TextField()
    designer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rooms"
    )
    number_of_seats = models.PositiveSmallIntegerField(default=0)
    occupation = models.BooleanField(default=False)
    date_creation = models.DateField(auto_now_add=True, db_index=True)
    book_room = models.ManyToManyField(User, related_name="booked_room")


    def __str__(self):
        return self.title

