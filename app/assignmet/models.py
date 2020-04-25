from django.db import models

from app.employee.models import Employee

class Assignmet(models.Model):
    assign_num = models.IntegerField(primary_key=True)
    assign_date = models.DateField()
    proj_num = models.IntegerField()
    emp_num = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    assign_job = models.IntegerField()
    assign_chg_hr = models.CharField(max_length=8)
    assign_hours = models.CharField(max_length=8)
    assign_charge = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.assign_job)


