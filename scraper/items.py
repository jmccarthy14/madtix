# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scraper.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from api.models import CLListing


class ScrapyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass


class CLListingItem(DjangoItem):
    django_model = CLListing