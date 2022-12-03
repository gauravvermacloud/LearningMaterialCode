from concurrent.futures import thread
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from datetime import datetime
import threading
import time
from my_logger import wrap
import config_reader

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


@wrap()
def myfunc():
    time.sleep(4)
    #We need to set the user header for the job
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$>>>>>>>>>>>>>> Every 1 sec " + str(datetime.now())+str(threading.get_ident()))


scheduler.add_job(myfunc, 'interval', seconds=1,
                  id='my_job_id', max_instances=1)

if(config_reader.is_scheduler_enabled):
    scheduler.start()
