# -*- coding: utf-8 -*-

# Scrapy settings for scrapping project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html


# IMPORT DJANGO SETTINGS
import os
import sys
import django

PROJECT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
sys.path.append(os.path.join(PROJECT_DIR, 'ScrapDjango'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'ScrapDjango.settings'

django.setup()


# SCRAPPING SETTINGS
BOT_NAME = 'scrapping'

SPIDER_MODULES = ['Scrapper.spiders']
NEWSPIDER_MODULE = 'Scrapper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Scrapper.pipelines.ScrappingPipeline': 300,
}
