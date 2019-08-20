# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@shared_task
def add(x, y):
    logger.info('ADD')
    time.sleep(7)
    return x + y

@shared_task
def mul(x, y):
    logger.info('MUL')
    time.sleep(7)
    return x * y

@shared_task
def xsum(numbers):
    return sum(numbers)