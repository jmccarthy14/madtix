# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scraper.org/topics/item-pipeline.html
from scrapy import log
from scraper.items import CLListingItem


def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    print filename
    print "test"
    project = imp.load_module('settings', f, filename, desc)

    setup_environ(project)

setup_django_env('/Users/Josh/projects/tix-web/tix')

class ScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class CLItemPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CLListingItem):
            log.msg("Processing "+item["title"])
            item.save()
