#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A demo of using lxml's xpath to parse html document
"""
from lxml import etree
import requests

grab_pattern_dict = {
    'img': {'//*[@id="J-detail-content"]/div//div/img': 'data-lazyload'},
    'price': {'//*[@id="jd-price"]': 'text'},
    'product': {'//*[@id="name"]/h1': 'text'},
    # 'parameter': {'//*[@id="product-detail-2"]/table': 'text'}
}
render_engine_api = 'http://10.19.8.61:32809'
send_data = {"url": "http://item.jd.com/1287950.html"}
r = requests.post(render_engine_api, data=send_data)
html_data = r.text

#要存到elasticsearch中的document
saved_doc = dict()
tree = etree.HTML(html_data)
for (key, value) in grab_pattern_dict.items():
    xpath_selector = value.keys()[0]#取出键中存放的xpath查询路径
    res = tree.xpath(xpath_selector)
    temp_list = []
    for item in res:
        attr = value.values()[0]
        if attr == 'text':
            parsed_value = item.text
        else:
            parsed_value = item.attrib[attr]
        temp_list.append(parsed_value)
    saved_doc[key] = temp_list

print saved_doc




