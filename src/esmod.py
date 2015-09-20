#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
"""
Common operation of elasticsearch
"""
node_list = [{"host": "10.19.8.61", "port": 9200}]
index_name = "tinycell"
type_name = "page_data"

es = Elasticsearch(node_list)

doc = {
    "author": "kimky",
    "text": "Elasticsearch: cool. bonsai cool.",
    "timestamp": datetime.now()
}

res = es.index(index=index_name, doc_type=type_name, body=doc)
print res['create']

res = es.get(index='test-index', doc_type='tweet', id=1)
print res['_source']

es.indices.refresh(index=index_name)

es.search(index=index_name, body={"query": {"match_all": {}}})
print "Got %d hits:" % res["hits"]["total"]

for hit in res["hits"]:
    print "%(timestamp)s %(author)s: %(text)s" % hit["_source"]