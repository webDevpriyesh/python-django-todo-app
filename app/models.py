from django.db import models

# Create your models here.
class TodoList(models.Model):
    text = models.CharField(max_length = 500)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text