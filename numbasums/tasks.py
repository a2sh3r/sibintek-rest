import logging

from celery import shared_task

from numbasums.models import Numbasum
from sibintek_rest.celery import app

logger = logging.getLogger(__name__)


@shared_task()
def task_execute(job_params):
    logger.info(f"Найден объект: {job_params}")
    try:
        numbasum = Numbasum.objects.get(pk=job_params['db_id'])
        numbasum.numba_sum = numbasum.first_numba + numbasum.second_numba
        numbasum.save()
    except Exception as e:
        logger.error(f"Объект с pk={job_params['db_id']} не найден.")
