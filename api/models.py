from django.db import models


class Attendees(models.Model):
    name = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Attendees"
        verbose_name_plural = "Attendees"
        ordering = ['-id']
