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
from .web_menu_model import AddNewWebMenu
from authentication.writer import write_error

current_file = 'Web_Menu_forms'


def addNew(request):
    success = 0
    failed = 0
    exist = 0
    keyid = request.POST['menuname']
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
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT menuName FROM web_menus WHERE menuName =%s", [keyid, ])

                if counter > 0:
                    exist += 1
                else:
                    gettime = datetime.datetime.now()
                    save_record = AddNewWebMenu()
                    save_record.category = request.POST['category'].capitalize()
                    save_record.menuName = request.POST['menuname'].lower()
                    save_record.menu_description = request.POST['displayname'].capitalize()
                    save_record.uniqueCode = int(round(time.time() * 1000))
                    save_record.created_by = request.session['userdata']['id']
                    save_record.modified_by = request.session['userdata']['id']
                    save_record.status_id = 0
                    save_record.record_status = 1
                    save_record.visibility = 0
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
            'msg': 'New record created successfully!',
            'classname': 'alert-primary p-2'
        }
    elif exist > 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'The detail(s) provided already exist, kindly '
                   'check your records to confirm this or try another.',
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
            menuName = request.POST['menuname']
            description = request.POST['displayname'].capitalize()

            status_id = 0
            keyid = request.POST['keyid']
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE web_menus SET menuName=%s, menu_description=%s, status_id=%s, "
                    "modified_by=%s, date_modified=%s, time_modified=%s "
                    "WHERE id=%s ",
                    [menuName, description, status_id, modified_by, date_modified, time_modified, keyid])
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
            'msg': 'The record was updated successfully.',
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
            visibility = request.POST['visibility']
            array_id = request.POST['keyid']
            lists = array_id.split(",")
            with connection.cursor() as cursor:
                for keyid in lists:
                    total += 1
                    cursor.execute("UPDATE web_menus SET status_id=%s, visibility=%s, "
                                   "modified_by=%s, date_modified=%s, "
                                   "time_modified=%s WHERE id=%s ",
                                   [status_id, visibility, modified_by, date_modified, time_modified, keyid])
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
                counter = cursor.execute("SELECT id FROM web_menus WHERE id =%s AND menuName=%s", [keyid, itemName])
                if counter > 0:
                    cursor.execute("DELETE FROM web_menus WHERE id=%s AND menuName=%s", [keyid, itemName])
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
            'msg': 'This record has been deleted and no longer exist.',
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
