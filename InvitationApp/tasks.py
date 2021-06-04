from __future__ import absolute_import, unicode_literals
from Invitation.celery import app
from celery import shared_task
import time

@shared_task
def test_celery():
    time.sleep(3)
    print("3 sec...")