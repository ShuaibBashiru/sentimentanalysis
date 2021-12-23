from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import pandas as pd
import datetime
from datetime import timedelta
import time
import json
import sys
import string
import random
import numpy as np
from django.db import connection, transaction
from .loans_model import AddNewLoan
from authentication.writer import write_error
from mailer.newpassword_mailer import admin_password as mailer
from authentication.query_columns import dictfetchall

current_file = 'Loan_account_forms'


def new_request(request):
    code = ''
    success = 0
    failed = 0
    exist = 0
    exist_msg = ''
    email = ''
    username = ''
    try:
        amount = round(float(request.POST['amount']), 2)
        duration = request.POST['duration']
        comment = request.POST['comment']
        email = request.POST['email']
        username = request.POST['username']

        personal_id = int(round(time.time() * 1000))
        keyid = request.session['userdata']['id']
        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(8))
        if request.method != 'POST':
            feedback = {
                'status': 'Invalid request',
                'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
                'classname': 'alert-danger p-2',
            }
            return JsonResponse(feedback, safe=False)

        else:
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT * FROM loan_request WHERE user_id =%s AND payment_status =%s", [keyid, 0])
                if counter >= 3:
                    exist += 1
                else:
                    gettime = datetime.datetime.now()
                    year = str(datetime.date.today().year)
                    month = str(datetime.date.today().month)
                    day = str(datetime.date.today().day)
                    days_of_month = int(duration) * 30
                    str_starting_date = "{}-{}-{}".format(year, month, day)
                    today_date = datetime.datetime.strptime(str_starting_date, "%Y-%m-%d")
                    starting_date = datetime.datetime.strptime(str_starting_date, "%Y-%m-%d")

                    expire_date = starting_date + timedelta(days=days_of_month)
                    break_exp_date = str(expire_date).split('-')
                    year_expire = break_exp_date[0]
                    month_expire = break_exp_date[1]
                    split_expire_day = break_exp_date[2].split()
                    day_expire = split_expire_day[0]

                    break_today_date = str(today_date).split('-')
                    today_year = break_today_date[0]
                    today_month = break_today_date[1]
                    split_today_day = break_today_date[2].split()
                    today_day = split_today_day[0]

                    save_record = AddNewLoan()
                    save_record.request_amount = amount
                    save_record.amount_paid = 0
                    save_record.user_id = keyid
                    save_record.attended_by = 0
                    save_record.duration = duration

                    save_record.year_apply = today_year
                    save_record.month_apply = today_month
                    save_record.day_apply = today_day

                    save_record.year_expire = year_expire
                    save_record.month_expire = month_expire
                    save_record.day_expire = day_expire

                    save_record.user_comment = comment
                    save_record.admin_comment = ''
                    save_record.uniqueCode = personal_id
                    save_record.status_id = 0
                    save_record.payment_status = 0
                    save_record.record_status = 1
                    save_record.visibility = 1
                    save_record.expire_date = expire_date
                    save_record.date_created = str(datetime.date.today())
                    save_record.time_created = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
                    save_record.date_modified = str(datetime.date.today())
                    save_record.time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))
                    save_record.save()
                    success += 1

    except Exception as e:
        success += 0
        write_error(current_file, e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': 'Hello, {}! We have received your loan request. One of our available managers will review and '
                   'determine the approval, loan amount eligibility and also communicate further via your email '
                   'address or phone number provided. Thanks!'.format(request.session['userdata']['surname']),
            'classname': 'alert-primary p-2'
        }

    elif exist > 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Hi, {}! You have too many loan requests you have not been cleared of, kindly contact our '
                   'support to help you further.'.format(request.session['userdata']['surname']),
            'classname': 'alert-danger p-2',
        }
    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
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
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }
        return JsonResponse(feedback, safe=False)

    else:
        try:
            gettime = datetime.datetime.now()
            year = str(datetime.date.today().year)
            month = str(datetime.date.today().month)
            day = str(datetime.date.today().day)
            date_modified = str(datetime.date.today())
            time_modified = str(datetime.time(gettime.hour, gettime.minute, gettime.second))

            get_duration = request.POST['duration']
            days_of_month = int(get_duration) * 30

            str_starting_date = "{}-{}-{}".format(year, month, day)
            today_date = datetime.datetime.strptime(str_starting_date, "%Y-%m-%d")
            starting_date = datetime.datetime.strptime(str_starting_date, "%Y-%m-%d")

            get_end_date = starting_date + timedelta(days=days_of_month)
            break_exp_date = str(get_end_date).split('-')
            break_today_date = str(today_date).split('-')

            extension = request.POST['extension'].lower()
            if extension == "continue":
                today_year = request.POST['year_apply']
                today_month = request.POST['month_apply']
                today_day = request.POST['day_apply']

                year_expire = request.POST['year_expire']
                month_expire = request.POST['month_expire']
                day_expire = request.POST['day_expire']
                expire_date = request.POST['expire_date']
                duration = request.POST['old_duration']
            else:
                today_year = break_today_date[0]
                today_month = break_today_date[1]
                split_today_day = break_today_date[2].split()
                today_day = split_today_day[0]

                year_expire = break_exp_date[0]
                month_expire = break_exp_date[1]
                split_expire_day = break_exp_date[2].split()
                day_expire = split_expire_day[0]
                expire_date = get_end_date
                duration = request.POST['duration']

            attended_by = request.session['userdata']['id']
            amount = round(float(request.POST['amount']), 2)
            uniqueCode = request.POST['uniqueCode']
            admin_comment = request.POST['admin_comment']

            status_id = 0
            keyid = request.POST['keyid']
            request_status = 1
            request_status_txt = 'Reviewing'
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE loan_request SET request_amount=%s, duration=%s, year_apply=%s, month_apply=%s, "
                    "day_apply=%s, year_expire=%s, month_expire=%s, day_expire=%s, admin_comment=%s, attended_by=%s, "
                    "expire_date=%s, request_status=%s, request_status_txt=%s, date_modified=%s, time_modified=%s "
                    "WHERE id=%s AND uniqueCode=%s ",
                    [amount, duration, today_year, today_month, today_day,
                     year_expire, month_expire, day_expire, admin_comment, attended_by,
                     expire_date, request_status, request_status_txt, date_modified, time_modified, keyid, uniqueCode])

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
            'msg': 'The record updated successfully, kindly await the user'"'s"' response on this update before you '
                   'give approval.',
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


def modify_update(request):
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

            uniqueCode = request.POST['uniqueCode']
            admin_comment = request.POST['admin_comment']
            listStatus = request.POST['listStatus']

            status_id = 0
            keyid = request.POST['keyid']
            request_status = 1
            request_status_txt = 'Reviewing'
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE loan_request SET request_status=%s, request_status_txt=%s, user_approval=%s, "
                    "date_modified=%s, WHERE id=%s AND uniqueCode=%s ",
                    [amount, duration, today_year, today_month, today_day,
                     year_expire, month_expire, day_expire, admin_comment, attended_by,
                     expire_date, request_status, request_status_txt, date_modified, time_modified, keyid, uniqueCode])

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
            'msg': 'The record updated successfully, kindly await the user'"'s"' response on this update before you '
                   'give approval.',
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
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
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
                    cursor.execute("UPDATE loan_request SET status_id=%s, "
                                   "attended_by=%s, date_modified=%s, "
                                   "time_modified=%s WHERE status_id=%s AND id=%s",
                                   [status_id, modified_by, date_modified, time_modified, 0, keyid])
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
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

        return JsonResponse(feedback, safe=False)

    else:
        try:
            keyid = request.POST['keyid']
            itemName = request.POST['itemName']
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT id FROM loan_request WHERE id =%s AND uniqueCode=%s",
                                         [keyid, itemName])
                if counter > 0:
                    cursor.execute("DELETE FROM loan_request WHERE id=%s AND uniqueCode=%s", [keyid, itemName])
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
            'msg': 'This record has been deleted and no longer exist,'
                   ' use the menu below to go back.',
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
