# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy import log
from batch.scrapy.items import CLListingItem


class ScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class CLItemPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CLListingItem):
            log.msg("Processing "+item["title"])
            item.save()
