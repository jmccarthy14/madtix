madtix
======

To run the cl scraper, first make sure you've updated your python deps `pip install -r requirements.txt`. 

Then, cd to the project root and sync your db `./manage.py syncdb`. You may need to clear your data first, using `./managepy sqlall api | ./managepy dbshell`.

Finally, `scrapy runspider batch/scrapy/spiders/craigslist.py`
