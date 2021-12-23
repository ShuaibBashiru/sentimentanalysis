from django.db import models

# Create your models here.


class AddNewWebMenu(models.Model):
    id = models.AutoField(primary_key=True)
    menuName = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    menu_description = models.TextField()
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
        db_table = 'web_menus'


