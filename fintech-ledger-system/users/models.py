from django.db import models

class UserRegister(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    
    def __str__(self):
        return self.first_name