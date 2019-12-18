# scrape.py

import os # standard imput stuff
import requests #

from bs4 import BeautifulSoup # also known as 'beautifulscraper'
from apscheduler.schedulers.blocking import BlockingScheduler # scheduler
from datetime import datetime # this will let us access current time
sched = BlockingScheduler();

def job_function():
    print "Hello World"


