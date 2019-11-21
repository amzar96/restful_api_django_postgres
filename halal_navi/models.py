from django.db import models


class User(models.Model):
    email = models.EmailField(max_length = 70)
    name = models.CharField(max_length = 250)
    country = models.CharField(max_length = 250)

    def __str__(self):
        return ("{}").format(self.name)


class Restaurant(models.Model):
    res_name = models.CharField(max_length = 50)
    city = models.CharField(max_length = 250)

    def __str__(self):
        return ("{}").format(self.res_name)


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, related_name = 'username', on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name = 'review', on_delete = models.CASCADE
    )
    review_text = models.CharField(max_length = 250)

    class Meta:
        unique_together = ['restaurant', 'user']
        ordering = ['user']

    def __str__(self):
        return ("({}) submit review for restaurant ({}) ").format(self.user, self.restaurant)
