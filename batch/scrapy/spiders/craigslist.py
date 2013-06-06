import re
from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from urlparse import urlparse, parse_qs
from batch.scrapy.items import CLListingItem


class CLListingsSpider(BaseSpider):

    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/sss?zoomToPosting=&query=tickets&srchType=T&minAsk=&maxAsk=&sort=date"]


    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        listings = hxs.select("//p")
        for listing_row in listings:
            listing_url = self.get_listing_url(listing_row)
            price_node = listing_row.select(".//span[@class='price']/text()")

            request = Request(listing_url, callback=self.parse_listing)

            if len(price_node) > 0:
                price = price_node[0].extract().replace("$", "")
                request.meta['price'] = price

            yield request

    def parse_listing(self, response):
        hxs = HtmlXPathSelector(response)
        title = hxs.select("//html/head/title/text()")[0].extract().encode("ascii", "replace").strip(" ")
        description = hxs.select("//section[@id='postingbody']/text()")[0].extract().strip(" ").replace("\n", "").replace("\t", "")
        link = response.url

        # get phone if available
        match = re.search("(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)", description)
        if match:
            phone = match.group(1)+"-"+match.group(2)+"-"+match.group(3)
        else:
            phone = None

        # get e-mail if available
        email_node = hxs.select("//section[@class='dateReplyBar']/a[1]/text()")
        if len(email_node) > 0:
            email = email_node.extract()[0].encode("ascii", "replace")
        else:
            email = None

        # get price if available
        if "price" in response.meta:
            price = response.meta['price']
        else:
            price = None

        location = self.get_listing_location(hxs)

        item = CLListingItem(title=title, description=description, link=link, price=price, location=location, email=email, phone=phone)
        return item

    def get_listing_url(self, listing_row):
        """
        Returns the listing url given the XPathSelector for a row on a craigstlist search page
        @type listing_row: scrapy.selector.XPathSelector
        @params listing_row: XPathSelector for a listing on a craigslist search page
        @return: string
        """
        listing_url = listing_row.select(".//a/@href")[0].extract()
        if listing_url[0] == "/":
            listing_url = "http://sfbay.craigslist.org" + listing_url

        return listing_url

    def get_listing_location(self, listing):
        """
        Try to determine the location of the listing
        @type listing: scrapy.selector.XPathSelector
        @param listing: XPathSelector for HTML of a Craigslist listing
        """

        # Strategy 1 - Get from mapaddress
        yahoo_map_url_node = listing.select("//p[@class='mapaddress']/small/a[2]/@href")
        if len(yahoo_map_url_node) > 0:
            yahoo_map_url = urlparse(yahoo_map_url_node[0].extract())
            yahoo_map_query_string = parse_qs(yahoo_map_url.query)
            addr = yahoo_map_query_string.get("addr")[0]
            csz = yahoo_map_query_string.get("csz")[0]
            country = yahoo_map_query_string.get("country")[0]
            address = addr+", "+csz+", "+country
            return address

        # Strategy 2 - Get From Title
        listing_title = listing.select("//h2[@class='postingtitle']")[0].extract()
        if listing_title.rfind("(") != -1:
            area = listing_title[listing_title.rfind("(")+1:listing_title.rfind(")")]
            return area

