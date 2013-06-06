from apscheduler.scheduler import Scheduler

sched = Scheduler()

@sched.interval_schedule(seconds=3)
def fetch_listings():
    print 'This job is run every three minutes.'

sched.start()

while True:
    pass