from concurrent.futures import thread
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from datetime import datetime
import threading
import time

# https://apscheduler.readthedocs.io/en/3.x/userguide.html
scheduler = BackgroundScheduler()

executors = {
    'default': ThreadPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 1
}


scheduler = BackgroundScheduler(
    executors=executors, job_defaults=job_defaults)


def myfunc():
    time.sleep(4)
    print("Every 1 sec " + str(datetime.now())+str(threading.get_ident()))


scheduler.add_job(myfunc, 'interval', seconds=1,
                  id='my_job_id', max_instances=1)

scheduler.start()
