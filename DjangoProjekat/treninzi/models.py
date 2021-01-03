from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Practice(models.Model):
    type = models.CharField(max_length=16)
    location = models.CharField(max_length=32)
    content = models.TextField(max_length=200)
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    hours = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(24)])
    minutes = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)



