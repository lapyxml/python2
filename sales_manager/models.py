from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.views import APIView

from sales_manager.utils import upload_to


class Book(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="название",
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="books"
    )
    date_publish = models.DateField(auto_now_add=True, db_index=True)
    # likes = models.ManyToManyField(User, related_name="liked_books", blank=True)
    avg_rate = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    rate = models.ManyToManyField(User,
                                  related_name="rated_book",
                                  blank=True,
                                  through="UserRateBook"
                                  )
    img = models.ImageField(blank=True, null=True, upload_to=upload_to)


    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        self.img.delete()
        super().delete()


class UserRateBook(models.Model):
    class Meta:
        unique_together = ("user", "book")

    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=4)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="rated_user")
    rate = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(5)])


class Comment(models.Model):
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=4,
        db_index=True,
        related_name="comments"
    )
    like = models.ManyToManyField(User, related_name="liked_comments", blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")


