from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES= [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed')
    ]
    title= models.CharField(max_length=200)
    description = models.TextField()
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Pending')
    completion_report=models.TextField(null=True,blank=True)
    worked_hours = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.title