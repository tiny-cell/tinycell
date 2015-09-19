#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    "author": "kimky",
    "text": "Elasticsearch: cool. bonsai cool.",
    "timestamp": datetime.now()
}

res = es.index(index='test-index', doc_type='tweet', id=1, body=doc)
print res['create']

res = es.get(index='test-index', doc_type='tweet', id=1)
print res['__source']

es.indices.refresh(index='test-index')

es.search(index='test-index', body={"query": {"match_all": {}}})
print "Got %d hits:" % res["hits"]["total"]

for hit in res["hits"]:
    print "%(timestamp)s %(author)s: %(text)s" % hit["_source"]

