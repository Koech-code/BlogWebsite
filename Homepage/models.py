from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=55, null=True)
    text = models.TextField(max_length=1000, null=True)
    # image = models.ImageField()

    def __str__(self):
        return self.title
    
class Feedback(models.Model):
    title = models.CharField(max_length=55, null=True)
    feedback = models.TextField(max_length=1000, null=True)
    # image = models.ImageField()

    def __str__(self):
        return self.title
    
class Testify(models.Model):
    title = models.CharField(max_length=55, null=True)
    testimony = models.TextField(max_length=1000, null=True)
    # image = models.ImageField()

    def __str__(self):
        return self.title