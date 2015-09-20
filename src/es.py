#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elasticsearch import Elasticsearch
from datetime import datetime

node_list = [{"host": "10.19.8.61", "port": 9200}]
es = Elasticsearch(node_list)

index_name = "test-index"
type_name  = "test"
doc = {
    "author": "Kevin",
    "text": "Elasticseach test",
    "timestamp": datetime.now()
}

res = es.index(index = index_name, doc_type = type_name, id = 1, body = doc)
print res['created']


res = es.get(index = index_name, doc_type = type_name, id = 1)
print res['_source']

es.indices.refresh(index = index_name)

res = es.search(index = index_name, body = {"query": {"match_all": {}}})
print "Got %d Hits" % res["hits"]["total"]

for hit in res["hits"]["hits"]:
    print "%(timestamp)s %(author)s: %(text)s" % hit["_source"]
