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
from forms.user_account_model import AddUserAccount
from authentication.writer import write_error
from mailer.newpassword_mailer import new_password_mailer as mailer
from mailer.newpassword_mailer import mailer_change
from authentication.query_columns import dictfetchall

current_file = 'User_account_forms'


def addNew(request):
    email_one = ''
    phone_one = ''
    firstname = ''
    code = ''
    success = 0
    failed = 0
    exist = 0
    exist_msg = ''
    failed = 0
    try:
        surname = request.POST['surname'].capitalize()
        firstname = request.POST['firstname'].capitalize()
        email_one = request.POST['email'].lower()
        phone_one = request.POST['phone']
        countryCode = request.POST['countryCode']
        gender = request.POST['gender']

        if request.POST['personalId'] == '':
            personal_id = int(round(time.time() * 1000))
        else:
            personal_id = request.POST['personalId']

        letters = string.ascii_lowercase
        code = ''.join(random.choice(letters) for i in range(8))
        if request.method != 'POST':
            feedback = {
                'status': 'Invalid request',
                'msg': 'Oops! You are making an '
                       'invalid request, please refresh or contact our support for further assistance',
                'classname': 'alert-danger p-2',
            }
            return JsonResponse(feedback, safe=False)

        else:
            with connection.cursor() as cursor:
                counter = cursor.execute("SELECT email_one, phone_one, personal_id FROM user_record WHERE email_one "
                                         "=%s OR phone_one=%s OR personal_id=%s", [email_one, phone_one, personal_id])
                if counter > 0:
                    row = dictfetchall(cursor)
                    return_email = row[0]['email_one'].lower()
                    return_phone = row[0]['phone_one'].lower()
                    return_person_id = row[0]['personal_id'].lower()
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
                    save_record = AddUserAccount()
                    save_record.surname = surname
                    save_record.firstname = firstname
                    save_record.othername = ''
                    save_record.countryCode = countryCode
                    save_record.email_one = email_one
                    save_record.phone_one = phone_one
                    save_record.gender = gender
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
        res = mailer(email_one, firstname, code)
        if res is True:
            feedback = {
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'New record was created successfully',
                'redirect': '/site/newpassword/' + str(email_one).lower() + '/' + code,
                'classname': 'alert-primary p-2'
            }

        else:
            feedback = {
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'New record was created successfully but we could not process e-mail notification right now, '
                       'please use forgot password link on login page to change password.',
                'classname': 'alert-warning p-2',
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


def updatename(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
            'status': 'Invalid request',
            'statusmsg': 'invalid request',
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
            emailid = request.POST['emailid'].lower()

            status_id = 0
            keyid = request.POST['keyid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET surname=%s, firstname=%s, othername=%s, modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [surname, firstname, othername, modified_by, date_modified, time_modified, keyid, emailid])
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


def updategender(request):
    success = 0
    failed = 0
    if request.method != 'POST':
        feedback = {
            'status': 'error',
            'statusmsg': 'invalid request',
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

            gender = request.POST['gender'].capitalize()
            emailid = request.POST['emailid'].lower()
            keyid = request.POST['keyid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET gender=%s, modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [gender, modified_by, date_modified, time_modified, keyid,
                                emailid])
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


def updatephone(request):
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
            phone_one = request.POST['phone_one']
            phone_two = request.POST['phone_two']
            emailid = request.POST['emailid'].lower()
            keyid = request.POST['keyid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET phone_one=%s, phone_two=%s, modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [phone_one, phone_two, modified_by, date_modified, time_modified, keyid,
                                emailid])
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


def updateaddress(request):
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

            address_one = request.POST['address_one']
            address_two = request.POST['address_two']
            emailid = request.POST['emailid'].lower()
            keyid = request.POST['keyid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET user_address_one=%s, user_address_two=%s, modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [address_one, address_two, modified_by, date_modified, time_modified, keyid,
                                emailid])
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


def updateemail(request):
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

            email_one = request.POST['email_one']
            email_two = request.POST['email_two']
            emailid = request.POST['emailid'].lower()
            keyid = request.POST['keyid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET email_two=%s, modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [email_two, modified_by, date_modified, time_modified, keyid,
                                emailid])
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


def jobrole(request):
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

            job_role = request.POST['job_role'].capitalize()
            job_department = request.POST['job_department'].capitalize()
            emailid = request.POST['emailid'].lower()
            keyid = request.POST['keyid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET job_role=%s, job_department=%s, modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [job_role, job_department, modified_by, date_modified, time_modified, keyid,
                                emailid])
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


def updatedob(request):
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
            dob = int(request.POST['dob'])
            print(dob)
            if dob == 1:
                mob_txt = 'Jan'
            elif dob == 2:
                mob_txt = 'Feb'
            elif dob == 3:
                mob_txt = 'March'
            elif dob == 4:
                mob_txt = 'April'
            elif dob == 5:
                mob_txt = 'May'
            elif dob == 6:
                mob_txt = 'June'
            elif dob == 7:
                mob_txt = 'July'
            elif dob == 8:
                mob_txt = 'August'
            elif dob == 9:
                mob_txt = 'September'
            elif dob == 10:
                mob_txt = 'October'
            elif dob == 11:
                mob_txt = 'November'
            elif dob == 12:
                mob_txt = 'December'
            else:
                mob_txt = 'None'

            mob = request.POST['mob']
            yob = request.POST['yob']
            emailid = request.POST['emailid'].lower()
            keyid = request.POST['keyid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET dob=%s, mob=%s, mob_txt=%s, yob=%s, modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [dob, mob, mob_txt, yob, modified_by, date_modified, time_modified, keyid,
                                emailid])
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


def updatepassword(request):
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
            password = request.POST['password']
            keyid = request.POST['keyid']
            emailid = request.POST['emailid']

            with connection.cursor() as cursor:
                cursor.execute("UPDATE user_record SET pwd_auth=%s, pwd_auth_hash=md5(%s), modified_by=%s, "
                               "date_modified=%s, time_modified=%s WHERE id=%s AND email_one =%s",
                               [password, password, modified_by, date_modified, time_modified, keyid,
                                emailid])
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
        email = request.POST['email']
        firstname = email
        res = mailer_change(email, firstname)
        if res is True:
            feedback = {
                'status': 'success',
                'statusmsg': 'success',
                'msg': 'Account password has been changed successfully',
                # 'redirect': '/site/newpassword/' + str(email).lower() + '/' + code,
                'classname': 'alert-primary p-2'
            }

        else:
            feedback = {
                'status': 'failed',
                'statusmsg': 'error',
                'msg': 'Account password has been changed successfully but we could not process e-mail notification '
                       'right now.',
                'classname': 'alert-warning p-2',
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
                    cursor.execute("UPDATE user_record SET status_id=%s, "
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
                counter = cursor.execute("SELECT id FROM user_record WHERE id =%s AND email_one=%s", [keyid, itemName])
                if counter > 0:
                    cursor.execute("DELETE FROM user_record WHERE id=%s AND email_one=%s", [keyid, itemName])
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
