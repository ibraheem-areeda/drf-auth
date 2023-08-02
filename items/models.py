from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Item (models.Model):
    name = models.CharField(max_length=64)
    purcheser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    price = models.IntegerField(default= 1)

    def __str__(self):
        return self.name
    
class Feedback (models.Model):
    purcheser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    feedbk = models.TextField(default="what is your feedback on this item")
    
    def __str__(self):
        return self.name
    
    


    

