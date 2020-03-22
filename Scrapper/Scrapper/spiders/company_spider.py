import scrapy

from ScrapDjangoApp.models import CompanyDetails

from ..items import CompanyDetailsItem
# from scrapy.linkextractors import LinkExtractor
# from scrapy.contrib.spiders import Rule

class SiteMapSpider(scrapy.Spider):

    name = "details"
    allowed_domains = ["websites.co.in/sitemap"]
    start_urls = ["https://websites.co.in/sitemap"]
    data_len = 10

    def parse(self, response):

        items = CompanyDetailsItem()

        all_data = response.css('table.table td ::text').extract()
        all_data = [str(r).lstrip().rstrip() for r in all_data]
        all_data[:] = (i for i in all_data if i != '')

        c_query = CompanyDetails.objects.all()

        if c_query:
            c_query.delete()

        business_name, website, cat, city = list(), list(), list(), list()
        for index in range(0, len(all_data), 3):

            if (index % 3) == 0:
                b_name, w_site = all_data[index].split("(")

                # business_name.append(str(b_name).lstrip().rstrip())
                # website.append(w_site[:-1])
                # cat.append(all_data[index+1])
                # city.append(all_data[index+2])

                items['Business_Name'] = str(b_name).lstrip().rstrip()
                items['Website'] = w_site[:-1]
                items['Category'] = all_data[index+1]
                items['City'] = all_data[index+2]

                if index == int(SiteMapSpider.data_len * 3):
                    break

            yield items

        # items['Business_Name'] = business_name
        # items['Website'] = website
        # items['Category'] = cat
        # items['City'] = city
        # yield items

