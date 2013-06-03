# Scrapy settings for scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scraper.org/topics/settings.html
#
import os

BOT_NAME = 'scrapy'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

ITEM_PIPELINES = [
    "scraper.pipelines.CLItemPipeline"
]


# http://stackoverflow.com/questions/4271975/access-django-models-inside-of-scrapy
def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)

    setup_environ(project)

current_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# setup_django_env(os.path.join(current_dir, '../tix'))
# setup_django_env("/Users/Josh/projects/tix-web/tix")

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraper (+http://www.yourdomain.com)'


