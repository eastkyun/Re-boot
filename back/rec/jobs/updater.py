from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import schedule_api


def start():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    # scheduler.add_job(schedule_api, 'interval', seconds=1)
    scheduler.add_job(schedule_api, 'cron', hour=9, minute=0, second=0)
    scheduler.start()
