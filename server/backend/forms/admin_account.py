from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import datetime
import time
import json
import sys
import string
import random
import numpy as np
from django.db import connection, transaction
from .admin_account_model import AddAdminAccount
from authentication.writer import write_error
from mailer.newpassword_mailer import admin_password as mailer
from authentication.query_columns import dictfetchall

current_file = 'Admin_account_forms'


def addNew(request):
    email_one = ''
    firstname = ''
    code = ''
    success = 0
    exist = 0
    exist_msg = ''
    failed = 0
    try:
        surname = request.POST['surname'].capitalize()
        firstname = request.POST['firstname'].capitalize()
        email_one = request.POST['email'].lower()
        phone_one = request.POST['phone']
        countryCode = request.POST['countryCode']

        if request.POST['personalId'] == '':
            personal_id = int(round(time.time() * 1000))
        else:
            personal_id = request.POST['personalId']

        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(8))
        if request.method != 'POST':
            feedback = {
                'status': 'Invalid request',
                'msg': 'Something went wrong!, please refresh or contact our support for further assistance',
                'classname': 'alert-danger p-2',
            }
            return JsonResponse(feedback, safe=False)

        else:
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT email_one, phone_one FROM admin_record WHERE email_one =%s OR "
                                         "phone_one=%s", [email_one, phone_one])
                if counter > 0:
                    row = dictfetchall(cursor)
                    cursor.close()
                    return_email = row[0]['email_one'].lower()
                    return_phone = row[0]['phone_one'].lower()
                    if email_one == return_email and phone_one == return_phone:
                        exist_msg = 'Email address and phone number provided already exist, kindly try another or use ' \
                                    'forgot password link on login page to retrieve password and log in. '
                    elif email_one.lower() == return_email:
                        exist_msg = 'Email address provided already exist, kindly try another or use ' \
                                    'forgot password link on login page to retrieve password and log in. '
                    elif phone_one == return_phone:
                        exist_msg = 'Phone number provided already exist, kindly try another.'

                    elif personal_id.lower() == return_person_id:
                        exist_msg = 'Personal ID provided already exist, kindly try another.'
                    else:
                        exist_msg = 'Something went wrong! Please confirm if this record already exist or try again.'

                    exist += 1
                else:
                    gettime = datetime.datetime.now()
                    save_record = AddAdminAccount()
                    save_record.pwd_auth = surname
                    save_record.surname = surname
                    save_record.firstname = firstname
                    save_record.countryCode = countryCode
                    save_record.email_one = email_one
                    save_record.phone_one = phone_one
                    save_record.personal_id = personal_id
                    save_record.uniqueCode = int(round(time.time() * 1000))
                    save_record.created_by = 0
                    save_record.modified_by = 0
                    save_record.status_id = 0
                    save_record.record_status = 1
                    save_record.visibility = 1
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
            'msg': 'New record was created successfully',
            'redirect': '/site/newpassword/' + str(email_one).lower() + '/' + code,
            'classname': 'alert-primary p-2'
        }
    elif exist > 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': exist_msg,
            'classname': 'alert-danger p-2',
        }
    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def update(request):
    success = 0
    failed = 0
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
            date_modified = str(datetime.date.today())
            time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            modified_by = request.session['userdata']['id']

            surname = request.POST['surname'].capitalize()
            firstname = request.POST['firstname'].capitalize()
            othername = request.POST['othername'].capitalize()
            email_one = request.POST['email'].lower()
            phone_one = request.POST['phone']
            countryCode = request.POST['countryCode']

            status_id = 0
            keyid = request.POST['keyid']
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE admin_record SET surname=%s, firstname=%s, othername=%s, "
                    "email_one=%s, phone_one=%s, countryCode=%s, status_id=%s, "
                    "modified_by=%s, date_modified=%s, time_modified=%s "
                    "WHERE id=%s ",
                    [surname, firstname, othername, email_one, phone_one, countryCode,
                     status_id, modified_by, date_modified, time_modified, keyid])
                transaction.commit()
                updated = cursor.rowcount
                if updated > 0:
                    success += 1
                else:
                    failed += 1
        except Exception as e:
            failed += 1
            write_error(current_file, e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'Record updated successfully.',
            'classname': 'alert-primary p-2'
        }
    else:
        feedback = {
            'status': 'Failed',
            'msg': 'Something went wrong or this record no longer exist. '
                   'Kindly confirm this update and try again.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def update_status(request):
    success = 0
    failed = 0
    total = 0
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
            date_modified = str(datetime.date.today())
            time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
            modified_by = request.session['userdata']['id']
            status_id = request.POST['listStatus']
            array_id = request.POST['keyid']
            lists = array_id.split(",")
            with connection.cursor() as cursor:
                for keyid in lists:
                    total += 1
                    cursor.execute("UPDATE admin_record SET status_id=%s, "
                                   "modified_by=%s, date_modified=%s, "
                                   "time_modified=%s WHERE id=%s ",
                                   [status_id, modified_by, date_modified, time_modified, keyid])
                    transaction.commit()
                    updated = cursor.rowcount
                    if updated > 0:
                        success += 1
                    else:
                        failed += 1
        except Exception as e:
            failed += 1
            write_error(current_file, e)

    if failed == 0 and success == 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'success': success,
            'total': total,
            'failed': failed,
            'msg': 'We could not process your request(s) because the selected one(s) are already activated, '
                   'please confirm the unsuccessful record(s) below.',
            'classname': 'alert-danger p-2',
        }

    elif failed > 0 and success == 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'success': success,
            'total': total,
            'failed': failed,
            'msg': 'Something went wrong! refresh and try again or contact our support',
            'classname': 'alert-danger p-2',
        }

    elif failed == 0 and success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'success': success,
            'total': total,
            'failed': failed,
            'msg': 'All record updated successfully',
            'classname': 'alert-primary p-2'
        }

    elif total > success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'success': success,
            'total': total,
            'failed': failed,
            'msg': 'We could not process all your requests because some selected one(s) are already exist, '
                   'please confirm the unsuccessful record(s) below.',
            'classname': 'alert-warning p-2'
        }

    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'success': success,
            'total': total,
            'failed': failed,
            'msg': 'Technical issue! refresh and try again or contact our support',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def delete(request):
    success = 0
    failed = 0
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
            keyid = request.POST['keyid']
            itemName = request.POST['itemName']
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT id FROM admin_record WHERE id =%s AND email_one=%s", [keyid, itemName])
                if counter > 0:
                    cursor.execute("DELETE FROM admin_record WHERE id=%s AND email_one=%s", [keyid, itemName])
                    transaction.commit()
                    deleted = cursor.rowcount
                    cursor.close()
                    if deleted > 0:
                        success += 1
                    else:
                        failed += 1
                else:
                    failed += 1

        except Exception as e:
            failed += 1
            write_error(current_file, e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'This record has been deleted and no longer exist',
            'classname': 'alert-danger p-2'
        }
    else:
        feedback = {
            'status': 'Failed',
            'statusmsg': 'error',
            'msg': 'Oops! Something went wrong or this record no longer exist.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


