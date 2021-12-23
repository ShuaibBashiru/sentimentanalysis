from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
import time
import json
import sys
import random
import datetime
import numpy as np
from django.db import connection, transaction
from authentication.query_columns import dictfetchall
from .feedback_model import AddFeedBack
from authentication.writer import write_error

current_file = 'Feedback_forms'


def addNew(request):
    success = 0
    failed = 0
    exist = 0
    keyid = request.POST['email']
    comment = request.POST['comments']
    category_id = request.POST['category']
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance',
            'classname': 'alert-danger p-2',
        }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            gettime = datetime.datetime.now()
            year = str(datetime.date.today().year)
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            str_starting_date = "{}-{}-{}".format(year, month, day)
            today_date = datetime.datetime.strptime(str_starting_date, "%Y-%m-%d")
            break_today_date = str(today_date).split('-')
            today_year = break_today_date[0]
            today_month = break_today_date[1]
            split_today_day = break_today_date[2].split()
            today_day = split_today_day[0]
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT username FROM feedback WHERE username =%s AND category_id =%s AND "
                                         "comments=%s", [keyid, comment, category_id])

                if counter > 0:
                    exist += 1
                else:
                    save_record = AddFeedBack()
                    save_record.username = request.POST['email']
                    save_record.category_id = request.POST['category']
                    save_record.comments = request.POST['comments']
                    save_record.uniqueCode = int(round(time.time() * 1000))
                    save_record.created_by = 0
                    save_record.modified_by = 0
                    save_record.status_id = 0
                    save_record.record_status = 1
                    save_record.visibility = 0
                    save_record.year_date = today_year
                    save_record.month_date = today_month
                    save_record.day_date = today_day
                    save_record.date_created = str(datetime.date.today())
                    save_record.time_created = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
                    save_record.date_modified = str(datetime.date.today())
                    save_record.time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
                    save_record.save()
                    success += 1
        except Exception as e:
            failed += 1
            write_error(current_file, e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'Your message has been submitted successfully, thanks!',
            'classname': 'alert-primary p-2'
        }
    elif exist > 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'The comment provided already exist on your email, please try another',
            'classname': 'alert-danger p-2'
        }
    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong! refresh and try again or contact support',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)

