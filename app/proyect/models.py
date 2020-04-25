from django.db import models

from app.employee.models import Employee

class Project(models.Model):
    proj_num = models.IntegerField(primary_key=True)
    proj_name = models.CharField(max_length=15)
    proj_value = models.IntegerField()
    proj_balance = models.IntegerField()
    emp_num = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.proj_name)