from django.db import models

# Create your models here.


class AddFeedBack(models.Model):
    id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    comments = models.TextField()
    username = models.CharField(max_length=100)
    uniqueCode = models.CharField(max_length=50)
    status_id = models.IntegerField()
    record_status = models.IntegerField()
    visibility = models.IntegerField()
    year_date = models.CharField(max_length=50)
    month_date = models.CharField(max_length=50)
    day_date = models.CharField(max_length=50)
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    date_created = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'feedback'


