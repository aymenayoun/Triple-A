from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Expenses(models.Model):
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateField(default=now)
    description=models.TextField()
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    category=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.category
    
    class Meta:
        ordering=['-date'] #sort by date 
        
class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural='Categories' #plural name
        