from django.db import models


class AddNewLoan(models.Model):
    id = models.AutoField(primary_key=True)
    request_amount = models.FloatField()
    amount_paid = models.FloatField()
    user_id = models.IntegerField()
    attended_by = models.IntegerField()
    year_apply = models.CharField(max_length=50)
    month_apply = models.CharField(max_length=50)
    day_apply = models.CharField(max_length=50)
    year_expire = models.CharField(max_length=50)
    month_expire = models.CharField(max_length=50)
    day_expire = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    user_comment = models.TextField()
    admin_comment = models.TextField()
    uniqueCode = models.CharField(max_length=50)
    status_id = models.IntegerField()
    payment_status = models.IntegerField()
    record_status = models.IntegerField()
    visibility = models.IntegerField()
    date_created = models.DateField()
    expire_date = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'loan_request'

