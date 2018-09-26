# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import uuid


class MeiziPipeline(object):
    def process_item(self, item, spider):
        # 创建一个不重复的文件保存图片
        path = './img/'+str(uuid.uuid4())+item['img_type']
        data = item['img'].body
        with open(path, 'wb') as f:
            f.write(data)
            print('OK')
