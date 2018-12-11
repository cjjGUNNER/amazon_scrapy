# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
class AmazonPipeline(object):
    def __init__(self):
        self.file = open('amazon.csv', 'wb')
    def process_item(self, item, spider):
        if item['title']:
            item['title'] = item['title'].strip()
            # print(item['title'])
            line = json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + b'\n'
            self.file.write(line)
            return item
        else:
            raise DropItem("Missing title in %s" % item)
        return item
