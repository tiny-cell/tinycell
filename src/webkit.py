# -*- coding: utf-8 -*-
import sys
# print(sys.getdefaultencoding())
reload(sys)
##sys.setdefaultencoding('gbk')
sys.setdefaultencoding('utf8')
from ghost import Ghost
from bs4 import BeautifulSoup
import re
from flask import Flask, request

app = Flask(__name__)

# with ghost.start() as session:
#    page, extra_resources = session.open("http://www.baidu.com")
#    assert page.http_status == 200 and 'baidu' in ghost.content
#    assert page.http_status == 200
# ghost = Ghost(wait_timeout=120)
# url = "http://www.baidu.com"

# URL = 'https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-11208661518.19.F74K2B&id=45521390248&scene=taobao_shop'
# URL = 'https://item.taobao.com/item.htm?spm=a219r.lm874.14.159.cBgMyp&id=520610383067&ns=1&abbucket=13#detail'
# xpath = '//*[@id="attributes"]/ul'
# DefaultAgent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2'
AGENT = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; Shuame)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12F70 Safari/600.1.4 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Shuame; .NET4.0E; .NET4.0C; InfoPath.2)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; GWX:DOWNLOADED)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2251.0 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/8.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/8.0; .NET4.0C; .NET4.0E; InfoPath.3; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Creative AutoUpdate v1.41.09)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3; Shuame)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0E; .NET4.0C; Tablet PC 2.0; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; GWX:RESERVED)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95  Safari/537.36'
]


def rand_agent():
    from random import choice
    return choice(AGENT)


DOWNLOADIMAGES = False
TIMEOUT = 300

ghost = Ghost()


def get_raw_page(url):
    # with ghost.start() as session:
    agent = rand_agent()
    with ghost.start(user_agent=agent, wait_timeout=TIMEOUT, viewport_size=(2560, 1440),
                     download_images=DOWNLOADIMAGES) as session:
        session.open(url)
        # session.wait_for_page_loaded()
        session.wait_for_selector('#summary-price .dd #jd-price')
        session.evaluate(
            '''var delay = 100;//in milliseconds
var scroll_amount = 200;// in pixels
var interval;
function scroller() {
    var old = document.body.scrollTop;
    document.body.scrollTop += scroll_amount;
    if (document.body.scrollTop == old) {
        clearInterval(interval);
    }
}
function scrollToBottom()
{
  interval = setInterval("scroller()",delay);
}

scrollToBottom()''')
# scrollToBottom()''', expect_loading=True)

        # session.wait_for_page_loaded()

#         session.wait_for_page_loaded()
        # page, resources = session.wait_for_page_loaded()
        # write_to_file(session.content)
        return session.content


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        output = get_raw_page(url)
        return output
    else:
        return '''
    <!doctype html>
    <html>
    <body>
    <form action='/' method='post'>
         <input type='text' name='url' size='50'>
         <input type='submit' value='fetch!'>
    </form>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
