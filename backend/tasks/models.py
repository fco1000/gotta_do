from django.db import models

# Create your models here.
class Task(models.Model):
    user_id = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    details = models.CharField(max_length=300,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reminder = models.DateTimeField(blank = True,null = True)
    is_completed = models.BooleanField(default = False)

    def __str__(self):
        return str(f'{self.title} is {self.is_completed}')