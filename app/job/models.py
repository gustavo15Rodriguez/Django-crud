from django.db import models

class Job(models.Model):
    job_code = models.IntegerField(primary_key=True)
    job_description = models.CharField(max_length=50)
    job_chg_hour = models.CharField(max_length=15)
    job_last_update = models.DateField()

    def __str__(self):
        return '{}'.format(self.job_description)
