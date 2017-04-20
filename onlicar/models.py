from django.db import models

# Create your models here.
class data_table(models.Model):
    driver_name=models.CharField(max_length=150)
    insurance=models.IntegerField()
    tax=models.IntegerField()
    mot=models.IntegerField()
    phone_no=models.CharField(max_length=150)
    lastMotDate=models.CharField(max_length=150)
    model_name=models.CharField(max_length=150)

    def __str__(self):
        return str(self.pk)
    
    
    