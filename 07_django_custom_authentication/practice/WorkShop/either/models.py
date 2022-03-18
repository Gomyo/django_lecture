from django.db import models

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=100)
    blue = models.CharField(max_length=50)
    red = models.CharField(max_length=50)

class Comment(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='comments')
    pick = models.CharField(max_length=5)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content
