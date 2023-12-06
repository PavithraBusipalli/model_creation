from django.db import models

# Create your models here.

class Dept_name(models.Model):
    dname=models.CharField(max_length=100,primary_key=True)

class Dept_info(models.Model):
    dname=models.ForeignKey(Dept_name,on_delete=models.CASCADE)
    dept_id=models.IntegerField
    dept_head=models.CharField(max_length=20)
    dept_url=models.URLField()
    #dept_file=models.FileField()
    dept_start_date=models.DateField(default='2023-12-10')
    dept_start_time=models.DateTimeField()

class Dept_Faculty_info(models.Model):
    dept_id=models.ForeignKey(Dept_info,on_delete=models.CASCADE)
    faculty_name=models.CharField(max_length=10)
    subj=models.CharField(max_length=20)