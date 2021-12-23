from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os
import datetime
import time
import json
import sys
import string
import random
import numpy as np
import urllib.request
from django.db import connection, transaction
from authentication.query_columns import dictfetchall
from authentication.writer import write_error
from mailer.forgotpassword_mailer import new_password


def update_password(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            gettime = datetime.datetime.now()
            date_modified = str(datetime.date.today())
            time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            password = request.POST['password']
            email = request.POST['email']
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE business_record SET "
                    "pwd_auth_hash=MD5(%s), pwd_auth=%s, date_modified=%s, time_modified=%s "
                    "WHERE email_one=%s ",
                    [password, password, date_modified, time_modified, email])
                transaction.commit()
                updated = cursor.rowcount
                if updated > 0:
                    success += 1
                else:
                    failed += 1
        except Exception as e:
            failed += 1
            write_error('Change password', e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'Your password has been changed successfully, log in to continue',
            'redirect': '/site/signin/',
            'classname': 'alert-primary p-2'
        }
    else:
        feedback = {
            'status': 'Failed',
            'statusmsg': 'error',
             'msg': 'Something went wrong, please try again later.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def validate_email_id(request):
    try:
        email = request.POST['email']
        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(8))
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM business_record WHERE "
                                     "email_one = %s LIMIT 1", [email, ])
            row = dictfetchall(cursor)
            if counter > 0:
                business_name = row[0]['businessName']
                res = new_password(email, business_name, code)
                if res is True:
                    feedback = {
                        'status': 'success',
                        'statusmsg': 'success',
                        'msg': 'New record created successfully! now redirecting..',
                        'redirect': '/site/newpassword/' + str(request.POST['email']).lower() + '/' + code,
                        'classname': 'alert-primary p-2'
                    }
                else:
                    feedback = {
                        'status': 'failed',
                        'statusmsg': 'error',
                        'msg': 'We could not process mail notification request right now, please try again later',
                        'classname': 'alert-danger p-2',
                    }

            else:
                feedback = {
                   'status': 'failed',
                   'msg': 'The account email provided do not exist with us, please try again or create an account',
                   'classname': 'alert-danger p-2'
                    }
    except Exception as e:
        write_error('Forgot password', e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong or this record no longer exist. '
                   'Kindly try again using forgotten password.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)
