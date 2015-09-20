var casper = require('casper').create({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X)',
    viewportSize: {width: 1024, height: 768}
});

//casper.userAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X)');


casper.start('http://item.jd.com/1287950.html', function () {
    //this.scrollToBottom();
    //onPageInitialized()
    this.echo(Object.keys(this));                                                 //成功时调用的函数
    //this.echo(Object.prototype(this));
    //this.echo(this.getHTML());                                                 //成功时调用的函数
    this.echo(this.getTitle());                                                 //成功时调用的函数
});

casper.run();
