import sys
import os
from django.http import HttpResponse, JsonResponse
import json
import datetime
import time
from numpy import random
import numpy as np
import pandas as pd
import csv
import urllib.request
from django.db import connection
from authentication.query_columns import dictfetchall
from authentication.writer import write_error
from textblob import TextBlob
import random
import base64

current_file = "Statistics"


def get_group(request):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT distinct(year_date) FROM feedback ORDER BY year_date DESC")
            row = dictfetchall(cursor)
            if counter > 0:
                feedback = {
                    'status': 'success',
                    'statusmsg': 'success',
                    'msg': '',
                    'result': row,
                    'classname': '',
                }
            else:
                feedback = {
                    'status': 'failed',
                    'statusmsg': 'error',
                    'msg': 'There is no record here yet.',
                    'classname': 'alert-danger p-2',
                }

    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }

    return JsonResponse(feedback, safe=False)


def get_stats(request):
    try:
        year = request.GET['year']
        month = request.GET['month']
        stats_info = get_stats_info(year, month)
        stats_categ = get_stats_categ(year, month)
        feedback = {
            'status': 'success',
            'statusmsg': 'success',
            'msg': '',
            'result': '',
            'stats_categ': stats_categ,
            'stats_info': stats_info,
            'classname': '',
        }
    except Exception as e:
        write_error(current_file, e)
        feedback = {
            'status': 'failed',
            'statusmsg': 'error',
            'msg': 'Something went wrong!, please refresh or contact our support for further assistance.',
            'classname': 'alert-danger p-2',
        }
    return JsonResponse(feedback, safe=False)


def get_stats_info(year, month):
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    count = 0
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT * FROM feedback WHERE year_date =%s AND month_date=%s", [year, month])
            row = dictfetchall(cursor)
            for i in row:
                txt = i['comments']
                count += 1
                analysis = TextBlob(txt)
                polarity += analysis.sentiment.polarity
                if analysis.sentiment.polarity == 0.00:
                    neutral += 1
                    num_neutral += 1
                elif analysis.sentiment.polarity < 0.00:
                    negative += 1
                    num_negative += 1
                elif analysis.sentiment.polarity > 0.00:
                    positive += 1
                    num_positive += 1

            positive = 100 * float(positive) / float(count)
            negative = 100 * float(negative) / float(count)
            neutral = 100 * float(neutral) / float(count)
            positive = format(positive, '.2f')
            negative = format(negative, '.2f')
            neutral = format(neutral, '.2f')

            if counter > 0:
                feedback = {
                    'positive': positive,
                    'negative': negative,
                    'neutral': neutral,
                    'num_positive': num_positive,
                    'num_negative': num_negative,
                    'num_neutral': num_neutral,
                }
                result = feedback
            else:
                result = 0
    except Exception as e:
        write_error(current_file, e)
        result = 'E-0'
    return result


def get_stats_categ(year, month):
    try:
        with connection.cursor() as cursor:
            counter = cursor.execute("SELECT t2.category_name, count(t1.category_id) as TotalItems FROM feedback t1 "
                                     "INNER JOIN items_category t2 ON t1.category_id=t2.id WHERE t1.year_date = %s "
                                     "AND t1.month_date=%s GROUP BY t1.category_id", [year, month])
            row = dictfetchall(cursor)

            if counter > 0:
                result = row
            else:
                result = 0
    except Exception as e:
        write_error(current_file, e)
        result = 'E-0'
    return result
