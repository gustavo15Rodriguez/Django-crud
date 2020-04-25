from django.db import models

from app.job.models import Job

class Employee(models.Model):
    emp_num = models.IntegerField(primary_key=True)
    emp_lname = models.CharField(max_length=20)
    emp_fname = models.CharField(max_length=20)
    emp_initial = models.CharField(max_length=3, null=True, blank=True)
    emp_hiredate = models.DateField()
    job_code = models.ForeignKey(Job, null=True, blank=True, on_delete=models.CASCADE)
    emp_years = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.emp_fname, self.emp_lname)
