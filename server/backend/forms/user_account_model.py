from django.db import models


class AddUserAccount(models.Model):
    id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    othername = models.CharField(max_length=50)
    email_one = models.CharField(max_length=50)
    phone_one = models.CharField(max_length=50)
    countryCode = models.CharField(max_length=30)
    gender = models.CharField(max_length=50)
    personal_id = models.CharField(max_length=50)
    uniqueCode = models.CharField(max_length=50)
    status_id = models.IntegerField()
    record_status = models.IntegerField()
    visibility = models.IntegerField()
    created_by = models.IntegerField()
    modified_by = models.IntegerField()
    date_created = models.DateField()
    time_created = models.TimeField()
    date_modified = models.DateField()
    time_modified = models.TimeField()

    class Meta:
        db_table = 'user_record'

