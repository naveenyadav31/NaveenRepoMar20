# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from ScrapDjangoApp.models import CompanyDetails


class CompanyDetailsItem(DjangoItem):
    """
    Define a item based on django model CompanyDetails
    """
    django_model = CompanyDetails
