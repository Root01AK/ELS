from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.TextField()
    phone = models.CharField(max_length=12)
    def __str___(self):
        return self.name