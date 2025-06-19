from django.db import models

class Journal(models.Model):
    moods = (
        ('Happy','happy'),
        ('Fine','fine'),
        ('Groggy','groggy'),
        ('Crappy','crappy'),
    )
    user_id = models.CharField(max_length=100)
    date = models.DateTimeField(auto_created=True)
    title = models.CharField(max_length = 100, default = "Untitled")
    content = models.CharField(max_length=1000)
    mood = models.CharField(max_length = 20,choices = moods)

    def __str__(self):
        return str(f'{self.title}, updated on {self.date}')