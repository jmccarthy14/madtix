# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import re
from django.db import IntegrityError
from scrapy import log
from api.models import Ticket
from batch.scrapy.items import CLListingItem


class ScrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class CLItemPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CLListingItem):
            log.msg("Processing "+item["title"])
            try:
                item.save()

                filter = False
                if item['price'] <= 1:
                    filter = True
                elif item['location'] and self.all_upper_case(item['location']):
                    filter = True
                elif any(stop_word in item['title'].lower() for stop_word in ["want", "wanted", "need", "trade", "would like", "would love", "wtb", "cheap", "games"]):
                    filter = True

                if not filter:
                    self.add_as_ticket(item)
            except IntegrityError as e:
                # already stored
                log.msg("Already stored this item")


    def all_upper_case(self, str):
        has_lower_case = False
        return re.search("[a-z]", str) is None


    def add_as_ticket(self, item):
        ticket = Ticket(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            pickup_location=item['location'],
            seller_email_address=item['email'],
            seller_phone=item['phone'],
            external_src='craigslist',
            external_listing_url=item['link']
        )
        ticket.save()