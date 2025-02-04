from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TASK (models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    task_name=models.CharField(max_length=100)
    task_description=models.TextField(null=True,blank=True)
    task_status=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

