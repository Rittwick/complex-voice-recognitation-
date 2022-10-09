from django.db import models

class PhrasalVerb(models.Model):
    verb = models.CharField(max_length=50)
    meaning = models.CharField(max_length=300)
    is_bookmarked = models.BooleanField(default=False) 
    

class Example(models.Model):
    verb = models.ForeignKey(PhrasalVerb, on_delete=models.CASCADE)
    sentence = models.CharField(max_length=300)

