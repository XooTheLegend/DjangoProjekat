from django.db import models

class Practice(models.Model):
    type = models.TextField()
    location = models.TextField()
    hours = models.IntegerField()
    minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)



