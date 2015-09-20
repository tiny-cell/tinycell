# -*- coding: utf-8 -*-
import sys
# print(sys.getdefaultencoding())
reload(sys)
##sys.setdefaultencoding('gbk')
sys.setdefaultencoding('utf8')
import re
from flask import Flask, request

app = Flask(__name__)

from elasticsearch import Elasticsearch

node_list = [{"host": "10.19.8.61", "port": 9200}]
es = Elasticsearch(node_list)

index_name = "test-index"
type_name  = "test"











@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        output = get_raw_page(url)
        return output
    else:
        res = es.search(index = index_name, body = {"query": {"match_all": {}}})
# print "Got %d Hits" % res["hits"]["total"]

# for hit in res["hits"]["hits"]:
#     print "%(timestamp)s %(author)s: %(text)s" % hit["_source"]
        return '''
    <!doctype html>
    <html>
    <body>
    <h1> Hello </h1>
    ''' + str(res)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
