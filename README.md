madtix
======

To run the cl scraper, first make sure you've updated your python deps `pip -r requirements.txt`. Then, cd to the project root and sync your db `./manage.py syncdb`. Finally, `scrapy runspider /batch/scrapy/spiders/craigslist.py`