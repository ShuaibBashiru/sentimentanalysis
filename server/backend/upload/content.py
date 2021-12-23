from django.http import HttpResponse, JsonResponse
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
from .content_model import AddContent
from authentication.writer import write_error
from mailer.newpassword_mailer import new_password_mailer as mailer
from mailer.newpassword_mailer import mailer_change
from authentication.query_columns import dictfetchall
import mimetypes

# from .models import file_upload

current_file = 'Upload'


def file_upload_preview(request):
    success = 0
    failed = 0
    filename = ''
    load_output = ''
    accepted_file = 'text/csv'
    accepted_file2 = 'application/vnd.ms-excel'
    try:
        filename = str(int(round(time.time() * 1000)))
        if request.method != 'POST':
            feedback = {
                'status': 'Invalid request',
                'statusmsg': 'error',
                'msg': 'Something went wrong!, please refresh or contact our support for further assistance',
                'classname': 'alert-danger p-2',
            }
            return JsonResponse(feedback, safe=False)

        else:
            form = request.FILES['fileupload']
            location = 'static/tmp_uploaded/'
            file_url = location + filename + '.csv'
            file_type = mimetypes.guess_type(file_url, strict=True)

            if str(file_type[0]) != str(accepted_file) and str(file_type[0]) != str(accepted_file2):
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'Something went wrong! This file type is not an acceptable format, please try another file '
                           'format such as (CSV).',
                    'classname': 'alert-danger p-2',
                }
                return JsonResponse(feedback, safe=False)

            else:
                fs = FileSystemStorage(location=location)
                fs.save(filename + '.csv', form)
                read_file = pd.read_csv(file_url)
                df = pd.DataFrame(read_file)
                json_output = df.to_json(orient="records")
                load_output = json.loads(json_output)
                success += 1

    except Exception as e:
        failed += 1
        write_error(current_file, e)

    if success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'result': load_output,
            'total': len(load_output),
            'filename': filename + str('.csv'),
            'msg': 'The preview of this file is shown below, click on Upload button to upload this file',
            'classname': 'alert-warning p-2'
        }
    else:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'total': 0,
            'msg': 'Something went wrong! refresh and try again or contact support',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def file_upload(request):
    success = 0
    failed = 0
    exist = 0
    total = 0
    failed_list = []
    index_num = 0
    load_output = ''
    load_output_success = ''
    file_url = ''
    category_id = request.POST['category_id']

    try:
        gettime = datetime.datetime.now()
        filename = request.POST['filename']
        location = 'static/tmp_uploaded/'
        file_url = location + filename
        data = pd.read_csv(file_url)
        df = pd.DataFrame(data)
        json_output = df.to_json(orient="records")
        load_output_success = json.loads(json_output)

        if request.method != 'POST':
            feedback = {
                'status': 'Invalid request',
                'statusmsg': 'error',
                'msg': 'Something went wrong! please refresh or contact our support for further assistance',
                'classname': 'alert-danger p-2',
            }
            return JsonResponse(feedback, safe=False)

        else:
            for f in data.itertuples():
                index_num = f.Index
                total += 1
                title = f.title
                faults = f.faults
                solution_one = f.solution_one
                solution_two = f.solution_one
                solution_three = f.solution_one

                with connection.cursor() as cursor:
                    counter = cursor.execute("SELECT * FROM contents WHERE "
                                             "title =%s AND faults=%s OR solution_one=%s", [title,  faults, solution_one])
                    if counter > 0:
                        exist += 1
                        failed_list.append(index_num)
                    else:
                        save_record = AddContent()
                        save_record.category_id = category_id
                        save_record.title = title
                        save_record.faults = faults
                        save_record.solution_one = solution_one
                        save_record.solution_two = solution_one
                        save_record.solution_three = solution_one
                        save_record.uniqueCode = int(round(time.time() * 1000))
                        save_record.created_by = 0
                        save_record.modified_by = 0
                        save_record.status_id = 1
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
    return_data = pd.read_csv(file_url)
    df = pd.DataFrame(return_data, index=failed_list)
    json_output = df.to_json(orient="records")
    load_output = json.loads(json_output)
    if failed == 0 and success == 0 and exist > 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'success': success,
            'total': total,
            'exist': exist,
            'failed': failed,
            'result': load_output,
            'msg': 'We could not process your request(s) because the selected one(s) are already exist, '
                   'please confirm the unsuccessful record(s) below.',
            'classname': 'alert-danger p-2',
        }

    elif failed > 0 and success == 0 and exist == 0:
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'success': success,
            'total': total,
            'exist': exist,
            'failed': failed,
            'result': load_output,
            'msg': 'Something went wrong! refresh and try again or contact our support',
            'classname': 'alert-danger p-2',
        }

    elif failed == 0 and success > 0 and exist == 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'success': success,
            'total': total,
            'exist': exist,
            'failed': failed,
            'result': load_output_success,
            'msg': 'All record uploaded successfully',
            'classname': 'alert-primary p-2'
        }

    elif total > success > 0:
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'success': success,
            'total': total,
            'exist': exist,
            'failed': failed,
            'result': load_output,
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
            'exist': exist,
            'failed': failed,
            'result': load_output,
            'msg': 'Technical issue! refresh and try again or contact our support',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)
