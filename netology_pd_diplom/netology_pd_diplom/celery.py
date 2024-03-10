from __future__ import absolute_import, unicode_literals
import os
from celery import Celery, shared_task
from celery.result import AsyncResult
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netology_pd_diplom.settings')
app = Celery('netology_pd_diplom')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def sort_iter(data):
    return sorted(data)


@app.task
def get_sum(data):
    return sum(data)
